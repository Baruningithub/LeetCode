from collections import defaultdict
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        d = defaultdict(int)
        
        for i in nums:
            d[i] += 1
            if d[i] == 2:
                ans ^= i
        
        return ans