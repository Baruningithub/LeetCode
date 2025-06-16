class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        ms_bit = 1

        for i in range(1,n+1):
            if i == ms_bit * 2:
                ms_bit = i
            dp[i] = 1 + dp[i - ms_bit]

        return dp

