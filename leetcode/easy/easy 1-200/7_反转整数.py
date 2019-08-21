def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if str(x)[0] == '-':
        sum_str = ''
        for i in list(str(x)[1:])[::-1]:
            sum_str = sum_str + str(i)
        if int('-' + sum_str) < -2**31:
            return 0
        else:
            return int('-' + sum_str)
    else:
        sum_str = ''
        for i in list(str(x)[:])[::-1]:
            print(i)
            sum_str = sum_str + str(i)
        if int(sum_str) > 2**31:
            return 0
        else:
            return int(sum_str)

if __name__ == '__main__':
    print(reverse(-30))
