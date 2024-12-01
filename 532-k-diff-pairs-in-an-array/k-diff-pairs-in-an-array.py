class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
            if  k == 0:
                diffPairs = 0
                numbers = {}
                
                for num in nums:
                    if num in numbers:
                          numbers[num] += 1
                    else:
                         numbers[num] = 1
                for num in numbers:
                    if numbers[num] > 1:
                        diffPairs += 1

                return diffPairs
    
            diffPairs = 0
            numbers = set(nums)
            
            for num in numbers:
                if num + k  in numbers:
                    diffPairs += 1
            return diffPairs
    