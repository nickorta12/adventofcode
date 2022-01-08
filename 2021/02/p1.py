with open("input") as f:
    lines = f.read().splitlines()

x, y = 0, 0


def forward(i):
    global x
    x += i


def down(i):
    global y
    y += i


def up(i):
    global y
    y -= i


funcs = {"forward": forward, "down": down, "up": up}

for line in lines:
    cmd, num = line.split()
    funcs[cmd](int(num))

print(f"{x=}, {y=}")
print(f"total={x * y}")
