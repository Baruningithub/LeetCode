class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        min_ = nums[0]

        for i in nums:
            if i <= min_:
                min_ = i
            else:
                diff = max(diff, i - min_)

        return diff
