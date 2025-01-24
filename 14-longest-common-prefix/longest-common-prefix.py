class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_prefix = strs[0]  

        for str in strs[1:]: 
            min_length = min(len(str), len(first_prefix))
            
            first_prefix = first_prefix[:min_length]

            for i in range(min_length):
                if str[i] != first_prefix[i]:
                    first_prefix = first_prefix[:i]  
                    break  

        return first_prefix