class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return None
        right = len(height) - 1
        left = 0
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    results = Solution()
    print(results.maxArea([1, 3, 2, 5, 25, 24, 5]))
