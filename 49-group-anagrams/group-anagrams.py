class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} # will be sorted_word key -> list of words 

        for word in strs:
            sorted_word = "".join(sorted(word))
            seen[sorted_word] = seen.get(sorted_word, []) + [word]

        return [seen[group] for group in seen]