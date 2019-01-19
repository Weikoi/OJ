def guessNumber(guessed_num, n):
    """
    :type n: int
    :rtype: int
    """

    def guess(mid, guess_num=guessed_num):
        if mid == guess_num:
            return 0
        elif mid > guess_num:
            return -1
        else:
            return 1

    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            high = mid - 1
        elif guess(mid) == 1:
            low = mid + 1
    return None


if __name__ == '__main__':
    print(guessNumber(6, 10))
