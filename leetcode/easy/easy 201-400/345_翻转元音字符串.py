def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    word = 'aeiouAEIOU'
    filter_word = [i for i in s if i in word]

    ret = list(s)
    for idx, val in enumerate(ret):
        if val in word:
            ret[idx] = filter_word.pop()
            print(ret)
    return ''.join(ret)


if __name__ == '__main__':
    print(reverseVowels('hello'))