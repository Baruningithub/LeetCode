class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "" : return t

        count = Counter(t)

        for i in s:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        
        return list(count.keys())[0]