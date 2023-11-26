class Solution:
    def makeGood(self, s: str) -> str:
        stack = [ "!" ] # stop marker
        for c in s:
            other = chr(ord(c) ^ 32) # ASCII values of lower-/uppercase letters are 32 apart
                                     # that means they differ by just one bit
            if stack[-1] == other:
                stack.pop()
            else:
                stack.append(c)

        stack.pop(0) # remove stop marker
        return "".join(stack)
