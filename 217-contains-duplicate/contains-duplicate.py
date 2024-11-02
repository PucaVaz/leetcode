class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        
        for number in nums:
            if number not in visited:
                visited.add(number)
                continue
        
        if len(visited) < len(nums):
            return True

        return False