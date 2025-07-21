class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        last_checked = s[0]
        count = 1

        for i in s[1:]:
            if i != last_checked:
                last_checked = i
                count = 0
            
            count += 1
            if count > 2:
                continue
            
            result += i

        return result
