class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0 
        piles.sort(reverse=True)

        # looks at every other coin 
        for i in range(1, 2 * len(piles) // 3, 2): 
            ans += piles[i]

        return ans 