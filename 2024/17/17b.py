import math


def combo_operand(x, reg_A, reg_B, reg_C):
    if x < 4:
        res = x
    elif x == 4:
        res = reg_A
    elif x == 5:
        res = reg_B
    elif x == 6:
        res = reg_C
    else:
        raise ValueError("Invalid operand")

    return res


def machine(program, A0, B0, C0):
    A = A0
    B = B0
    C = C0

    instruction_pointer = 0
    o_list = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        literal_operand = program[instruction_pointer + 1]

        if opcode == 0:
            tmp = A >> combo_operand(literal_operand, A, B, C)
            A = tmp
        elif opcode == 1:
            tmp = B ^ literal_operand
            B = tmp
        elif opcode == 2:
            tmp = combo_operand(literal_operand, A, B, C) % 8
            B = tmp
        elif opcode == 3:
            if A != 0:
                instruction_pointer = literal_operand
                continue
        elif opcode == 4:
            tmp = B ^ C
            B = tmp
        elif opcode == 5:
            tmp = combo_operand(literal_operand, A, B, C) % 8
            o_list.append(tmp)
        elif opcode == 6:
            tmp = A >> combo_operand(literal_operand, A, B, C)
            B = tmp
        elif opcode == 7:
            tmp = A >> combo_operand(literal_operand, A, B, C)
            C = tmp
        else:
            raise ValueError("Invalid opcode")

        instruction_pointer += 2

    return o_list


if __name__ == "__main__":

    program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 0, 5, 5, 3, 0]

    # last 3 output digits of machine are determined by first 3 digits of A in octal
    # second last 3 output digits of machine are determined by second 3 digits of A in octal

    # 1st 3 octal digits are 560
    # 2nd 3 octal digits are 053
    # 3rd 3 octal digits are 275
    # 4th 3 octal digits are 602
    # 5th 3 octal digits are 505
    # last octal digit is 2

    known_oct_digits = ""

    for _ in range(math.ceil(len(program) / 3)):
        num_unknown_digits = len(program) - len(known_oct_digits)

        exp = min(3, num_unknown_digits)

        for tmp in range(8**exp):
            if exp == 3:
                oct_str = f"{known_oct_digits}{oct(tmp)[2:]:0>3}"
            elif exp == 2:
                oct_str = f"{known_oct_digits}{oct(tmp)[2:]:0>2}"
            elif exp == 1:
                oct_str = f"{known_oct_digits}{oct(tmp)[2:]}"
            else:
                raise ValueError("Invalid exponent")

            A_init = int(oct_str, 8)
            A = A_init

            out_list = machine(program, A, 0, 0)

            if out_list[-len(oct_str) :] == program[-len(oct_str) :]:
                print(
                    f"{A_init:016} {oct(A_init)} {','.join([str(x) for x in out_list])}"
                )
                known_oct_digits += oct_str[-3:]
                break
