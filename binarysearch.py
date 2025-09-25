def solve(nums, target):
    l = -1
    r = len(nums)
    while r - l > 1:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m
    if nums[l] != target:
        return -1
    else:
        return l
