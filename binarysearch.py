nums = [int(e) for e in input().split()]
target = int(input())
l = -1
r = len(nums)
while r - l > 1:
    m = (l + r) // 2
    if nums[m] <= target:
        l = m
    else:
        r = m
if nums[l] != target:
    print(-1)
else:
    print(l)
