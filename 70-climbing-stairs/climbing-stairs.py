class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1


        prev_prev_step = 1  
        prev_step = 2      

        for _ in range(2, n):
            current_step = prev_prev_step + prev_step
            prev_prev_step, prev_step = prev_step, current_step

        return prev_step