from collections import Counter 
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        sorted_ = sorted(counter.items(), reverse=True)
        for x,y in (sorted_):
            if x == y:
                return x
        return -1