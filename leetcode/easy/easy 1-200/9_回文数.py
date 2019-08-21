def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    length = len(str(x))

    for i in range(1, int(length / 2) + 1):
        if str(x)[i - 1] != str(x)[-i]:
            return False
    return True


def isPalindrome2(x: int) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False

    num = x
    reversed_num = 0

    while (num != 0):
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num == x


if __name__ == '__main__':
    print(isPalindrome(121))
