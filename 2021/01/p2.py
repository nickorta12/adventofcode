nums = []
with open("input") as f:
    for line in f:
        nums.append(int(line))

bins = []
try:
    for i in range(len(nums)):
        bins.append(nums[i] + nums[i + 1] + nums[i + 2])
except IndexError:
    pass

inc = 0
prev = bins.pop(0)
for bin in bins:
    if bin > prev:
        inc += 1
    prev = bin

print(inc)
