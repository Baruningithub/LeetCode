class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0 
        piles.sort(reverse=True)

        # looks at every other coin 
        # for i in range(1, 2 * len(piles) // 3, 2): 
        #     ans += piles[i]
        
        for i in range(len(piles)//3):
            ans += piles[2*i + 1]

        return ans 