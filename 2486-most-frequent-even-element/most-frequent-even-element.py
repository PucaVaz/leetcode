class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        occurrence = {}

        for n in nums: 
            occurrence[n] = occurrence.get(n, 0) + 1

        top_occurrence = 0
        number = -1 

        for n in occurrence:
            if n % 2 == 0: 
                if occurrence[n] > top_occurrence:
                    number = n
                    top_occurrence = occurrence[n] 
                if occurrence[n] == top_occurrence:
                    if number > n:
                        number = n
        return number