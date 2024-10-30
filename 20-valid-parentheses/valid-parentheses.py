class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            ending_brackets = {')': '(', ']': '[', '}' : '{'}
            
            for char in s:
                if char in '([{':
                    stack.append(char)
                    continue
                elif char in ')]}':
                    if not stack or stack.pop() != ending_brackets[char]:
                        return False

            return len(stack) == 0