class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right+1):
            s = str(n)
            for i in s:
                if i == '0' or n % int(i) != 0:
                    break
            else:
                ans.append(n)
        
        return ans
