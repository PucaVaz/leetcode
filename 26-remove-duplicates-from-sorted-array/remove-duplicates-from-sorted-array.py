class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0 
        used = set()

        for i in range(len(nums)):
            if nums[i] not in used:
                nums[j] = nums[i]
                used.add(nums[i])
                j += 1 
            i += 1
            
        return j