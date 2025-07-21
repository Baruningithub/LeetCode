import re

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        v = ['a','e','i','o','u']

        for i in range(n):
            vowels = 0
            consonants = 0
            for j in range(i, n):
                if s[j] in v:
                    vowels += 1
                else:
                    consonants += 1

                if vowels == consonants and (vowels * consonants) % k == 0:
                    ans += 1

        return ans
