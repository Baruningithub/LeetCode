class Solution:
    def convertToBase7(self, n: int) -> str:
        if abs(n) < 7:
            return str(n)

        isNeg = n < 0
        ans = []
        a = abs(n)
        while a > 0:
            rem = a % 7
            ans.append(str(rem))
            a = a//7
        
        return "-"+''.join(reversed(ans)) if isNeg else ''.join(reversed(ans))

