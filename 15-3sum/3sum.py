
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            target = -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                current = nums[l] + nums[r]

                if current == target:
                    result.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1 
                    r -= 1

                elif current > target:
                    r -= 1 
                else:
                    l += 1 
                
        return result
    