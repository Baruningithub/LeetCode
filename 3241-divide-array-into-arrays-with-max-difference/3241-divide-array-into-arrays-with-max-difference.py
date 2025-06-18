class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        ans = []

        for i in range(0, l, 3):
            if nums[i+2] - nums[i] > k:
                return []
            ans.append([nums[i], nums[i+1], nums[i+2]])

        return ans
            