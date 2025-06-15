class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Make 'a' by replacing the first digit (not 9) with 9
        for ch in s:
            if ch != '9':
                a = s.replace(ch, '9')
                break
            else:
                a = s  # all digits are already 9

        # Make 'b' by replacing the first non-1 digit (if at first place), else replace first non-0/1 with 0
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    b = s.replace(ch, '0')
                    break
                else:
                    b = s  # all digits are 0 or 1

        return int(a) - int(b)
