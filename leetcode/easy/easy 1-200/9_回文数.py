def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    length = len(str(x))

    for i in range(1, int(length / 2) + 1):
        if str(x)[i-1] != str(x)[-i]:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome(121))
