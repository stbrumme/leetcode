class Solution:
    def decodeString(self, s: str) -> str:
        todo = []
        num  = ""
        text = ""
        for c in s:
            if   c == "[":
                todo.append((int(num), text))
                num  = ""
                text = ""
            elif c == "]":
                repeat, outer = todo.pop()
                text = outer + text * repeat
            elif c.isdigit():
                num += c
            else:
                text += c

        return text
