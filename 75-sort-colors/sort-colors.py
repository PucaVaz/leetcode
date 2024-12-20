class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        occurrences = {0: 0, 1: 0, 2: 0}

        for num in nums:
            occurrences[num] = occurrences.get(num, 0) + 1
                
        del nums[:]
        
        for color in range(3):
            for _ in range(occurrences[color]):
                nums.append(color)

        return nums