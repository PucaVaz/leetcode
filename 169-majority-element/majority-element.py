class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        visited = {}
        quorum = len(nums) / 2 

        for num in nums:
            visited[num] = 1 + visited.get(num, 0)
            if visited[num] > quorum:
                return num 
 