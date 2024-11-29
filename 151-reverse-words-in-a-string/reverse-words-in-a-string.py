class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        newWord = ""
        for i in range(len(s)): 
            if s[i] != " ":
                newWord += s[i]
                continue

            if s[i] == " " and newWord != "":
                words.append(newWord)
                newWord = ""

        if newWord != "":
            words.append(newWord)

        finalString = " ".join(reversed(words))
        
        return finalString