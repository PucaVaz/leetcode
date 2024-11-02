class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        
        for number in nums:
            if number in visited:
                return True
            visited.add(number) 
        
        if len(visited) < len(nums):
            return True

        return False