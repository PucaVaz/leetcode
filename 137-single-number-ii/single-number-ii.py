class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for num in seen:
            if seen[num] == 1:
                return num
        