import numpy as np


def encode_sequences(array, window_size=4):
    """Encode 2D array with a sliding window of 4 integers (-9 to 9)."""
    base = 19

    # Normalize the array values to range 0-18
    normalized = array + 9

    # Create sliding windows for each row
    sliding_windows = np.lib.stride_tricks.sliding_window_view(
        normalized, window_shape=(window_size,), axis=1
    )

    # Compute the encoded values using broadcasting and positional base conversion
    bases = base ** np.arange(
        window_size - 1, -1, -1
    )  # [base^3, base^2, base^1, base^0]
    encoded = np.tensordot(sliding_windows, bases, axes=(2, 0))

    return encoded


if __name__ == "__main__":
    divisor = 16777216
    num_iter = 2000
    test = True

    if test:
        secrets = [1, 2, 3, 2024]
    else:
        with open("input.txt", "r", encoding="UTF-8") as f:
            secrets = [int(line.strip()) for line in f]

    ones_digits = np.zeros((len(secrets), num_iter + 1), dtype=np.int8)

    for j, secret in enumerate(secrets):
        ones_digits[j, 0] = secret % 10

        for i in range(num_iter):
            secret = ((secret * 64) ^ secret) % divisor
            secret = ((secret // 32) ^ secret) % divisor
            secret = ((secret * 2048) ^ secret) % divisor

            # get the right most digit of secret
            ones_digits[j, i + 1] = secret % 10

    changes = ones_digits[:, 1:] - ones_digits[:, :-1]
    bananas = ones_digits[:, 1:]

    # %%
    # encode the 4-character sequences
    changes_char_seq = encode_sequences(changes)

    unique_char_seqs = np.unique(changes_char_seq)

    bananas_shifted = bananas[:, 3:]

    num_bananas = np.zeros(len(unique_char_seqs), dtype=int)

    for i, seq in enumerate(unique_char_seqs):
        if (i + 1) % 100 == 0:
            print(f"({i+1}/{len(unique_char_seqs)})", end="\r")
        for i_b, b in enumerate(bananas_shifted):
            tmp = np.where(changes_char_seq[i_b] == seq)[0]
            if len(tmp) > 0:
                num_bananas[i] += b[tmp[0]]

    print()
    print(num_bananas.max())
