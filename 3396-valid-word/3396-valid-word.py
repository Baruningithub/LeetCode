import re
class Solution:
    def isValid(self, word: str) -> bool:
        regex = '(?=.*[aeiou])(?=.*[^\daeiou])\w{3,}$'
        return re.match(regex, word, I) is not None