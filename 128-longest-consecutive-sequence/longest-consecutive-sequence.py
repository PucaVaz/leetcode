class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0 

        for num in nums:
            if num - 1 in nums:
                continue
            local_longest = 0
            i = 0 
            while (num + i) in nums:
                local_longest += 1
                i += 1 
            if local_longest > longest:
                longest = local_longest
        
        return longest
