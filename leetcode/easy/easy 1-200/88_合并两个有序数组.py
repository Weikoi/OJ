class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:  # 若nums1中最后一个元素大于nums2[]中最后一个元素
                nums1[m + n - 1] = nums1[m - 1]  # 则扩展后的列表最后一个元素是俩元素中最大的
                m -= 1  # nums1中元素-1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:  # 若nums1完了，nums2还没完
            nums1[:n] = nums2[:n]  # 把剩下nums2加在最开始


if __name__ == '__main__':
    results = Solution()
    num1 = [0]
    num2 = [2, 5, 6]
    results.merge(num1, 0, num2, 3)
    print(num1)
