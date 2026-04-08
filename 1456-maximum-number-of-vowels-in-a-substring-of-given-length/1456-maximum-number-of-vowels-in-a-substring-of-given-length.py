class Solution:
    def is_vowel(self, s: str)-> bool: #only single char
        return (s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u')
            

    def maxVowels(self, s: str, k: int) -> int:
        max_vowel_window_c = 0
        ans = 0
        n=len(s)

        for i in range(n):
            if self.is_vowel(s[i]):
                max_vowel_window_c += 1
            if (i >= k-1):
                ans = max(ans, max_vowel_window_c)
                max_vowel_window_c -= int(self.is_vowel(s[i-k+1]))

        return ans
    
    