class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)

        for i, n  in enumerate(nums):
            if(nums[i] != 0):
                if arr[n] > 1:
                    return n
                arr[n] += 1 

        i = 1
        while i < len(nums) + 1:
            if arr[i] > 1:
                return i         
            i += 1

        return 0

        return 0