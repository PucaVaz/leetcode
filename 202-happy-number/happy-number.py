import math 

class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1 or n==7:
            return True
        
        digit_list = [int(digit) for digit in str(n)]
        total_sum = 0
        for num in digit_list :
            total_sum += math.pow(num, 2)
            
        total_sum = int(total_sum)
        if total_sum == 1:
            return True
        elif total_sum > 6:
            return self.isHappy(total_sum)
        else:
            return False
        