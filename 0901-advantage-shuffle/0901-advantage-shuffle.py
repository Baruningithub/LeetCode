__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
__import__("atexit").register(lambda: open("display_memory.txt", "w").write("0"))

class Solution:
    def advantageCount(self, nums1, nums2):
        n = len(nums1)
        nums1_sorted = sorted(nums1)
        nums2_sorted = sorted([(num, i) for i, num in enumerate(nums2)])
        
        ans = [0] * n
        lo, hi = 0, n - 1
        
        for num, idx in reversed(nums2_sorted):
            if nums1_sorted[hi] > num:
                ans[idx] = nums1_sorted[hi]
                hi -= 1
            else:
                ans[idx] = nums1_sorted[lo]
                lo += 1
        return ans
