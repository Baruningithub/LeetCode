class Solution:
    def is_vowel(self, s: str)-> bool: #only single char
        vowels = {'a','e','i','o','u'}
        return s in vowels

    def maxVowels(self, s: str, k: int) -> int:
        window_count = 0
        ans = 0
        n=len(s)

        for i in range(n):
            if self.is_vowel(s[i]):
                window_count += 1
            if (i >= k-1):
                ans = max(ans, window_count)
                window_count -= int(self.is_vowel(s[i-k+1]))

        return ans
    
    