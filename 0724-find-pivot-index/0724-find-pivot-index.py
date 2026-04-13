class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)

        left_sum, right_sum = 0,0
        
        for i in range(n):
            curr = nums[i]
            right_sum = total - left_sum - curr

            if left_sum == right_sum:
                return i
            left_sum += curr
        
        return -1