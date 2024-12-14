class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff_1, diff_2 = [], []
        set_num1, set_num2 = set(nums1), set(nums2)
        for num in set_num1:
            if num not in set_num2:
                diff_1.append(num)
        for num in set_num2:
            if num not in set_num1:
                diff_2.append(num)
        return [diff_1, diff_2]