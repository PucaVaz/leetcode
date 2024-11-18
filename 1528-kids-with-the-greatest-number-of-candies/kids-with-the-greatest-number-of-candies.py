class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for candy in candies:
            result.append((lambda x: x + extraCandies >= max(candies))(candy))
        print(result)
        return result
                
