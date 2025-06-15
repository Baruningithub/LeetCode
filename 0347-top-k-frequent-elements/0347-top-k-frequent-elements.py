class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        counter = Counter(nums)
        ans = []
        c = 0

        sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        counter = {key: val for key, val in sorted_items}

        for key, val in counter.items():
            ans.append(key)
            c += 1
            if c == k:
                break

        return ans
