with open("input") as f:
    lines = f.read().splitlines()

x, y, aim = 0, 0, 0


def forward(i):
    global x, y
    x += i
    y += aim * i


def down(i):
    global aim
    aim += i


def up(i):
    global aim
    aim -= i


funcs = {"forward": forward, "down": down, "up": up}

for line in lines:
    cmd, num = line.split()
    funcs[cmd](int(num))

print(f"{x=}, {y=}")
print(f"total={x * y}")
