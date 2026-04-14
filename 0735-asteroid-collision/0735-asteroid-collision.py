class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for curr in asteroids:
            while stack and curr < 0 and stack[-1] > 0:
                if -curr > stack[-1]:
                    stack.pop()
                    continue
                elif -curr == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(curr)
        
        return stack