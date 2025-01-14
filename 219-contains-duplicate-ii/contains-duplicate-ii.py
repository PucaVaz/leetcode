class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        
        for i, num in enumerate(nums):
            is_present  = num in (nums[:i] + nums[i + 1:])
            if is_present:
                j = 0
                
                while j < k:
                    j += 1

                    if (0 <= (i + j) < len(nums) and nums[i + j] == num) or \
   (0 <= (i - j) < len(nums) and nums[i - j] == num):
                        return True
                
        return False
        