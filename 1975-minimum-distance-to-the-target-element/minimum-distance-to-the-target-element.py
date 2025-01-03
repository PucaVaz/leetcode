class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left = right = start 
        travel = 0
        while left >= 0 and right < len(nums): 
            if nums[left] == target or nums[right] == target:
                return travel 
            else:
                travel  += 1
                left    -= 1
                right   += 1

        if left >= 0:
            while left >= 0:
                if nums[left] == target:
                    return travel 
                else:
                    travel  += 1
                    left    -= 1
        if right < len(nums):
            while right < len(nums): 
                if nums[right] == target:
                    return travel 
                else:
                    travel  += 1
                    right   += 1
