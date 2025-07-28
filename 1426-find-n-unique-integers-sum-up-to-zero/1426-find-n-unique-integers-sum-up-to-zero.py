class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        
        index = 0
        ans = [0] * n
        for i in range(1, n//2+1):
            ans[index] = i
            index += 1
            ans[index] = -i
            index += 1

        return ans