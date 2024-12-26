class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        once = []
        for num in seen:
            if seen[num] == 1:
                once.append(num)

        return once