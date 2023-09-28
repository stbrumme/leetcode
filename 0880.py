class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # stack, each element is either a number or a letter
        todo = []
        for c in s:
            todo.append(int(c) if c.isdigit() else c)

        def length():
            result = 0
            for t in todo:
                if type(t) == str:
                    result += 1
                else:
                    result *= t
            return result

        for _ in range(len(todo)):
            k %= length()

            last = todo.pop()
            if type(last) == str:
                if k == 0:
                    return last
