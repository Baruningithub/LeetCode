class Solution:
    def kthCharacter(self, k: int) -> str:
        w = ['a']
        while len(w) < k:
            l = len(w)
            for i in range(l):
                char = chr(ord('a') + ((ord(w[i]) - ord('a') + 1) % 26))
                w.append(char)
        return w[k-1]