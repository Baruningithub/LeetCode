import sys
class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        if n < 10: return x

        ans = int(str(n)[::-1])

        if ans > (1 << 31) - 1: return 0

        return ans if x>0 else -ans
