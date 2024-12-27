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


if __name__ == "__main__":

    A = 32916674
    B = 0
    C = 0
    program = [2, 4, 1, 1, 7, 5, 0, 3, 1, 4, 4, 0, 5, 5, 3, 0]

    verbose = False

    instruction_pointer = 0

    out_list = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        literal_operand = program[instruction_pointer + 1]

        if verbose:
            print(instruction_pointer, opcode)
            print(A, B, C)

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
            out_list.append(tmp)
        elif opcode == 6:
            tmp = A >> combo_operand(literal_operand, A, B, C)
            B = tmp
        elif opcode == 7:
            tmp = A >> combo_operand(literal_operand, A, B, C)
            C = tmp
        else:
            raise ValueError("Invalid opcode")

        instruction_pointer += 2

        if verbose:
            print(A, B, C)
            print()

    print(",".join([str(x) for x in out_list]))
