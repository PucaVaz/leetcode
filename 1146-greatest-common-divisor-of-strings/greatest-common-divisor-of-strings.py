class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ""

        len_str1 = len(str1)
        len_str2 = len(str2)

        gcd = find_gcd(len_str1,len_str2)

        for i in range(gcd):
            c = str1[i] 
            b = str2[i]
            if b == c: 
                output += b
        


        # Valid str1 
        test1 = ""
        for i in range(len_str1//gcd):
            test1 += output 
        
        if str1 != test1:
            return ""
        
        # Valid str2
        test2 = ""

        for i in range(len_str2//gcd):
            test2 += output
        
        if str2 != test2:
            return ""
            
        return output
    
def find_gcd(a, b):
    if a == 0:
        return b
    return find_gcd(b % a, a)