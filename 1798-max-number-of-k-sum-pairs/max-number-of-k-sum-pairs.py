
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {} 
        pairs = 0
        half_k = k / 2
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num in list(count.keys()):
            if num == half_k:  
                pairs += count[num] // 2 
            elif k - num in count:  
                pairs += min(count[num], count[k - num])  
                count[k - num] = 0  
        
        return pairs