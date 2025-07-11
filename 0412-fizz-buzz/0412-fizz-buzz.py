class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0: return []
        l = []
        for i in range(1, n+1):
            if i%15 == 0:
                l.append("FizzBuzz")
            elif i%3 == 0:
                l.append("Fizz")
            elif i%5==0 and i%5==0:
                l.append("Buzz")
            else:
                l.append(str(i))
        return l            