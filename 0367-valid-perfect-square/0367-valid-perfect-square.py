class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        low = 2
        high = num//2
        while (low <= high):
            mid = (low+high)//2
            sq = mid * mid
            if sq == num:
                return True
            if sq > num:
                high = mid-1
            else:
                low = mid+1
        return False

