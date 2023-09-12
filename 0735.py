class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) >= 2 and stack[-2] > stack[-1] and stack[-2] * stack[-1] < 0:
                if abs(stack[-2]) == abs(stack[-1]):
                    stack.pop() # both explode
                    stack.pop()
                else:
                    if abs(stack[-2]) < abs(stack[-1]):
                        stack[-2] = stack[-1]
                    stack.pop()

        return stack
