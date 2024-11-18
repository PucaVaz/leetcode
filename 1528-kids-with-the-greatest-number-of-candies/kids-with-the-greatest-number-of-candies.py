class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        biggest_candy = max(candies)
        for candy in candies:
            if candy + extraCandies  >= biggest_candy:
                result.append(True)
                continue
            result.append(False)
        return result
                