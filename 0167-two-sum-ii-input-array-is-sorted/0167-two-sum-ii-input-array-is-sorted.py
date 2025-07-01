class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        low = 0
        high = len(n)-1
        
        while (high > low):

            if n[low] + n[high] == target:
                return [low+1,high+1]
            if n[low] + n[high] > target:
                high -= 1
            else:
                low += 1
        
        return []