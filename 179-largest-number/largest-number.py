from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=lambda x: str(x) * 10, reverse=True)

        return "0" if nums[0] == 0 else "".join(map(str, nums))

    def correctOrder(self, n):
        return int(str(n)[0])
