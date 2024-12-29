class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for n in range(n+1):
            ans.append(bin(n).count('1'))
        return ans