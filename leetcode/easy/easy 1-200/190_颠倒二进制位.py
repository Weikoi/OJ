class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print(bin(n))
        print(bin(n)[::-1][:-2])
        print('0b' + bin(n)[::-1][:-2])
        return int(bin(n)[2:].zfill(32)[::-1], base=2)



