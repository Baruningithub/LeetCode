# Intuition 💡
# To find the longest subarray of 1s after flipping at most K zeros, we can use a sliding window approach. We maintain a window that contains at most K zeros. As we expand the window to the right, if we exceed K zeros, we shrink from the left. The maximum window size during this process is our answer.

# Approach 🧠
# Step 1: Initialize Variables

# l = 0: Left pointer of sliding window
# r = 0: Right pointer of sliding window
# maxlen = 0: Maximum length of valid subarray found
# zeroes = 0: Count of zeros in current window
# Step 2: Expand Window to the Right

# Iterate with right pointer r from 0 to n-1
# For each position, potentially expand the window
# Step 3: Track Zeros in Window

# When nums[r] == 0, increment zeroes counter
# This represents using one of our K flips
# Step 4: Shrink Window if Invalid

# If zeroes > k, the window has too many zeros (exceeds our flip limit)
# Shrink from left:
# If nums[l] == 0, decrement zeroes (we're removing a zero from window)
# Increment l to move window right
# This maintains the invariant: window has at most K zeros
# Step 5: Update Maximum Length

# When zeroes <= k, the window is valid (all zeros can be flipped)
# Calculate window length: r - l + 1
# Update maxlen with maximum value seen
# Step 6: Move Right Pointer

# Increment r++ to expand window to the right
# Continue until we've processed all elements
# Step 7: Return Result

# maxlen contains the longest valid subarray length

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        maxWindow = 0
        zeroes = 0
        n = len(nums)

        while r < n:
            if nums[r] == 0:
                zeroes += 1
            
            if zeroes > k:
                if nums[l] == 0:
                    zeroes -=1
                l+=1

            # update the maxWindow for valid subarray
            if zeroes <= k:
                maxWindow = max(maxWindow, r-l+1)

            r += 1

        return maxWindow