class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counter = defaultdict(int)

        for i in s:
            counter[i]+=1

        for i in t:
            if i not in counter or counter[i] == 0:
                return False
            counter[i] -= 1

        return True

        