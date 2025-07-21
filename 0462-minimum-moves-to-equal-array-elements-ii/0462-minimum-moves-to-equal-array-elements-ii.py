class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        moves = 0

        for i in nums:
            moves+= abs(median - i)    

        return moves