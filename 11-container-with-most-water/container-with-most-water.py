class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1

        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l += 1
                continue
            r += -1

        return max_area