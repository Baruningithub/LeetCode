class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        winner = ["Bob", "Alice"]
        ans = min(x, y // 4)
        return winner[ans % 2]