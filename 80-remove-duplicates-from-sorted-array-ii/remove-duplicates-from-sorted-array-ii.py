class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0 
        used = {}

        for i in range(len(nums)):
            if nums[i] not in used or used[nums[i]] < 2:
                nums[j] = nums[i]
                used[nums[i]] = used.get(nums[i], 0) + 1
                j += 1 
            i += 1
            
        return j