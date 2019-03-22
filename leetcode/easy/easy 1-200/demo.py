def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last = 0
    now = 0
    for i in nums:
        last, now = now, max(last + i, now)
        print(last, now)
    return now


if __name__ == '__main__':
    print(rob([2, 1, 1, 2]))
