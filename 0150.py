class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+":
                sum = s[-2] + s[-1]
                s.pop()
                s.pop()
                s.append(sum)
            elif t == "-":
                diff = s[-2] - s[-1]
                s.pop()
                s.pop()
                s.append(diff)
            elif t == "*":
                mul = s[-2] * s[-1]
                s.pop()
                s.pop()
                s.append(mul)
            elif t == "/":
                divi = int(s[-2] / s[-1]) # float-to-int => rounds towards zero
                s.pop()
                s.pop()
                s.append(divi)
            else:
                s.append(int(t))

        return s[0]
