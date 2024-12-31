class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            list_x = [int(digit) for digit in str(x)]

        l = 0
        r = len(list_x) - 1 

        while l < r:
            if list_x[l] != list_x[r]:
                return False
            l += 1
            r -= 1

        return True