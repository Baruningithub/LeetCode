import re
class Solution:
    def isValid(self, word: str) -> bool:
        regex = r'^(?=.*[AEIOUaeiou])(?=.*[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z])[A-Za-z0-9]{3,}$'
        return re.match(regex, word) is not None