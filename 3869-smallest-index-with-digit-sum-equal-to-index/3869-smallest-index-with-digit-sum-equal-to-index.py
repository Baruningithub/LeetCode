class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            L = list(str(nums[i]))
            a = sum(int(i) for i in L)
            if a == i:
                return i
            

        return -1