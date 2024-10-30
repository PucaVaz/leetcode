class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        
        for number in arr:
            if number in occurrences:
                occurrences[number] += 1
                continue
            else:
                occurrences[number] = 1
        if len(set(occurrences.values())) < len(occurrences):
            return False
        return True