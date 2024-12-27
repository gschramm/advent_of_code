divisor = 16777216
num_iter = 2000

# secrets = [1, 10, 100, 2024]

with open("input.txt", "r", encoding="UTF-8") as f:
    secrets = [int(line.strip()) for line in f]

total = 0

for secret in secrets:
    for i in range(num_iter):
        secret = ((secret * 64) ^ secret) % divisor
        secret = ((secret // 32) ^ secret) % divisor
        secret = ((secret * 2048) ^ secret) % divisor

    total += secret
    print(secret)

print()
print(total)
