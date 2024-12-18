class Solution:
    def compress(self, chars: List[str]) -> int:
        occr = {}
        last_char = [None, 0]
        backup = chars[:]  
        del chars[:]  

        for char in backup: 
            occr[char] = occr.get(char, 0) + 1

            if last_char[0] == None:
                last_char[0], last_char[1] = char, 1
                chars.append(char[0])
            elif last_char[0] == char:  
                last_char[1] += 1
            elif last_char[0] != char:
                if last_char[1] > 1:
                    for digit in str(last_char[1]):
                        chars.append(str(digit))
                chars.append(char)
                last_char[0] = char
                last_char[1] = 1

        if last_char[1] > 1:
            for digit in str(last_char[1]):
                chars.append(str(digit))

        return len(chars)    