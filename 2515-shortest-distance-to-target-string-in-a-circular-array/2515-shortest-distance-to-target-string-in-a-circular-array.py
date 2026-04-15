class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        distance = float('inf')
        n = len(words)
        if words[startIndex] == target:
            return 0


        for i in range (n):
            if words[i] == target:
                distance = min(distance , 
                            # minimum distance for current match (as there coulbe multiple matches)
                            min(abs(i-startIndex), # liner distance
                            n - abs(i-startIndex))) #circular distance
        
        return -1 if distance > n else distance
