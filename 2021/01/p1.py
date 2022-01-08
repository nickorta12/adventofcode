nums = []
with open("input") as f:
    for line in f:
        nums.append(int(line))

prev = nums.pop(0)
inc = 0
for num in nums:
    if num > prev:
        inc += 1
    prev = num

print(inc)
