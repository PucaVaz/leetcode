class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude, current_sum = 0, 0

        for num in gain:
            current_sum += num
            if current_sum >= max_altitude:
                max_altitude = current_sum
        
        return max_altitude