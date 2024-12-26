class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occr = set()

        for num in nums:
            if num in occr:
                occr.remove(num)
            else: 
                occr.add(num)

        return occr.pop()