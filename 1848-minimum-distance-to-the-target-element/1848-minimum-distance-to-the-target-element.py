class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        abs_diff = float('inf')
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                abs_diff = min(abs_diff, abs(i-start))

        return abs_diff
               
