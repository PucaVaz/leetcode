class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 1)

        for i, n  in enumerate(nums):
            if(nums[i] != 0):
                arr[n] = 1

        i = 1
        while i < len(nums) + 1:
            if arr[i] == 0:
                return i         
            i += 1

        return 0