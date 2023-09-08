class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") # discard spaces
        s += "?"               # end-marker

        op   = "+"
        num  = 0
        todo = []
        # no brackets, almost sequential evaluation possible
        # note: * and / have hive precedence than + and -
        for c in s:
            if c.isnumeric():
                num = 10 * num + int(c)
            else:
                if   op == "+":
                    todo.append(+num)
                elif op == "-":
                    todo.append(-num)
                elif op == "*":
                    last = todo.pop()
                    todo.append(last * num)
                elif op == "/":
                    last = todo.pop()
                    div = last // num
                    if div < 0:
                        div = -(abs(last) // abs(num))
                    todo.append(div)
                op  = c
                num = 0

            if c == "?": # done
                return sum(todo)
