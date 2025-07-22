class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            digits = len(str(i))
            ans += int(digits % 2 == 0)
        return ans