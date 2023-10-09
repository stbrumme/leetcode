class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final(text):
            stack = []
            for c in text:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)

        return final(s) == final(t)
