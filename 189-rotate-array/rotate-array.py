class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        backup = nums[:]
        nums[:] = [0] * len(nums)

        for i, num in enumerate(backup):
            place = (i + k) % len(backup) 
            nums[place] = num