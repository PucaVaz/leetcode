class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = 0
        numbers = {}
        
        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        for num in numbers:
            if num + k in numbers:
                pairs += numbers[num] * numbers[num + k]
                
        return pairs
    