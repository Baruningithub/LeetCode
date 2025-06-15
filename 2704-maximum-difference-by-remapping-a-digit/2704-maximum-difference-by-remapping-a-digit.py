class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_str = str()
        min_str = str()
        
        for i in s:
            if i != '9':
                max_str = s.replace(i,'9')
                break
            else:
                max_str = s

        min_str = s.replace(s[0],'0')

        return int(max_str) - int(min_str)
        
