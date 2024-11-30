
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        songs = [0 for _ in range(0, 61)]
        pairs = 0
        for song in time:
            remainder = song % 60
            songs[remainder] += 1
    
        l = 1
        r = 59
        while l < r:
            pairs += songs[l] * songs[r]
            l += 1
            r -= 1
        
        if songs[0] > 1:
            pairs += songs[0] * (songs[0] - 1) // 2
        pairs += songs[30] * (songs[30] - 1) // 2

        return pairs
