class Solution:
    def smallestNumber(self, n: int) -> int:
        # if n == 1 : return 1

        # step = 1
        # while n >= step :
        #     step *= 2

        # return step - 1

        return  2**(int(log2(n)) +1)-1