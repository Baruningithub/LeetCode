class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        distance = n+1 #initailize min distance more that length

        if words[startIndex] == target:
            return 0

        for i in range (n):
            if words[i] == target:
                distance = min(distance , 
                            # minimum distance for current match (as there could be multiple matches)
                            min(abs(i-startIndex), # linear distance
                            n - abs(i-startIndex))) #circular distance
        
        return -1 if distance > n else distance
