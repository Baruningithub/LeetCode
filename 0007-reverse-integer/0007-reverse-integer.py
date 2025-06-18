import sys
class Solution:
    def reverse(self, x: int) -> int:

        n = abs(x)
        if n < 10: return x

        s = str(n)

        rev = s[::-1]

        ans = int(rev) if rev[0] != '0' else int(rev[1::])

        if ans>2**31-1 or ans < -2**31: return 0

        return ans if x>0 else -ans
