
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.m[old_val] -= 1
        self.nums2[index] += val
        self.m[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        c = 0
        for x in self.nums1:
            c += self.m[tot - x]
        return c

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)