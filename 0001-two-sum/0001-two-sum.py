class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        l = len(nums)

        for i in range(l):
            map[nums[i]] = i
        
        for i in range(l):
            x = target-nums[i]
            if x in map and map[x]!=i:
                return [i,map[x]]
        
        return None


