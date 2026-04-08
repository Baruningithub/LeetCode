class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        
        ans = float('-inf')  #lowest integer value 
        max_window_sum = 0
        
        for i in range(len(nums)):
            max_window_sum += nums[i]
            if (i >= k-1):
                ans = max(ans, max_window_sum)
                max_window_sum -= nums[i-k+1]   

        return ans/k