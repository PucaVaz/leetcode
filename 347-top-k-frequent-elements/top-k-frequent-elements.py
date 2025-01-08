class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1 

        bucket = [[]for _ in range(len(nums) +1)]

        for num, fre in frequency.items():
            bucket[fre].append(num)

        result = []

        for fre in range(len(nums), 0, -1):
            for num in bucket[fre]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result 
