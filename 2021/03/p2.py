from dataclasses import dataclass

with open("input") as f:
    lines = f.read().splitlines()


def get_indices(digits: list[str], check: str) -> list[str]:
    indices = []
    for i, v in enumerate(digits):
        if v == check:
            indices.append(i)
    return indices


@dataclass
class Indices:
    ones: list[int]
    zeros: list[int]


def get_indices(digits: list[str], index: int) -> Indices:
    indices = Indices([], [])
    for i, digit in enumerate(digits):
        if digit[index] == "1":
            indices.ones.append(i)
        elif digit[index] == "0":
            indices.zeros.append(i)
        else:
            raise ValueError()
    return indices


oxygen, co2 = 0, 0

digits = lines.copy()
for i in range(len(lines[0])):
    new_digits: list[str] = []
    indices = get_indices(digits, i)
    if len(indices.ones) >= len(indices.zeros):
        for index in indices.ones:
            new_digits.append(digits[index])
    else:
        for index in indices.zeros:
            new_digits.append(digits[index])
    digits = new_digits

    if len(digits) == 2:
        oxygen = int(digits[indices.ones[0]], 2)
        break

digits = lines.copy()
for i in range(len(lines[0])):
    new_digits: list[str] = []
    indices = get_indices(digits, i)
    if len(indices.ones) >= len(indices.zeros):
        for index in indices.zeros:
            new_digits.append(digits[index])
    else:
        for index in indices.ones:
            new_digits.append(digits[index])
    digits = new_digits

    if len(digits) == 2:
        co2 = int(digits[indices.zeros[0]], 2)
        break

total = oxygen * co2
print(f"{oxygen=} {co2=} {total=}")
