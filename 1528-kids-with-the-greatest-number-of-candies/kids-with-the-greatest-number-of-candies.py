class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        biggest_candy = max(candies)

        for candy in candies:
            result.append((lambda x: x + extraCandies >= biggest_candy)(candy))
        return result