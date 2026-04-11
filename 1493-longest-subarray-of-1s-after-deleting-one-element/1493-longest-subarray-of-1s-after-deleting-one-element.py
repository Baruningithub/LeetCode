class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        ans = 0
        n = len(nums)
        
        if n == 0 or 1 not in set(nums):
            return 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left)  # NOT +1

        return ans