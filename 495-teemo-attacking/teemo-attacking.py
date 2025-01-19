class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return False

        total = duration

        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])
        
        
        return total