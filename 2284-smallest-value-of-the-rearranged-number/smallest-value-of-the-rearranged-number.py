
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        sing =  (1 if num < 0 else 0)

        num = list(str(abs(num)))

        if sing:
            num.sort(reverse=True)
        else:
            num.sort()
        
        if num[0] == '0':
            for i in range(len(num)):
                if num[i] != '0':
                    num[0], num[i] = num[i], '0'
                    break
        result = int("".join(num))
   
        return result if not sing else -result 
