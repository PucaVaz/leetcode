class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = seen.get(n, 0) + 1

        result = []

        for n in seen:
            if seen[n] == 2:
                result.append(n)

        return result