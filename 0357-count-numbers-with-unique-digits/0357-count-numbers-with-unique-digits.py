class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n<=1:
            return 10**n
        
        curr = 9
        ans = 10

        for i in range(2, n+1):
            curr *= (10 - (i-1))
            ans += curr

        return ans