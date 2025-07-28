class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0 
        while n > 0:
            curr = n % 10

            s += curr
            p *= curr

            n //= 10

        return p - s