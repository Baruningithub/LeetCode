class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        low = 0
        high = len(nums) -1

        while low < high:
            result += nums[high] - nums[low]
            low += 1
            high -= 1
            
        return result