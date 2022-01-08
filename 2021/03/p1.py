with open("input") as f:
    lines = f.read().splitlines()

width = len(lines[0])
ones = [0] * width
zeros = [0] * width

for line in lines:
    for i, char in enumerate(line):
        if char == "1":
            ones[i] += 1
        elif char == "0":
            zeros[i] += 1
        else:
            raise ValueError()

gamma = []
epsilon = []
for one, zero in zip(ones, zeros):
    if one > zero:
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")

gamma = int("".join(gamma), 2)
epsilon = int("".join(epsilon), 2)

print(gamma * epsilon)
