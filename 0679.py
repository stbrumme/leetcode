class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # a,b,c are placeholders for operations
        def calc(formula):
            ops = [ "+", "-", "*", "/" ]
            for a in ops:
                for b in ops:
                    for c in ops:
                        f = formula
                        f = f.replace("a", a)
                        f = f.replace("b", b)
                        f = f.replace("c", c)
                        try:
                            if abs(eval(f) - 24) < 0.0000001: # allow small rounding errors
                                return True
                        except ZeroDivisionError:
                            continue
            return False


        s = [ str(c) for c in cards]
        for n in permutations(s):
            # ten distinct possibilities to add brackets
            if calc(n[0] + "a" + n[1] + "b" + n[2] + "c" + n[3]):
                return True
            if calc("(" + n[0] + "a" + n[1] + ")b" + n[2] + "c" + n[3]):
                return True
            if calc(n[0] + "a(" + n[1] + "b" + n[2] + ")c" + n[3]):
                return True
            if calc(n[0] + "a" + n[1] + "b(" + n[2] + "c" + n[3] + ")"):
                return True
            if calc("(" + n[0] + "a" + n[1] + ")b(" + n[2] + "c" + n[3] + ")"):
                return True
            if calc(n[0] + "a(" + n[1] + "b" + n[2] + "c" + n[3] + ")"):
                return True
            if calc(n[0] + "a((" + n[1] + "b" + n[2] + ")c" + n[3] + ")"):
                return True
            if calc(n[0] + "a(" + n[1] + "b(" + n[2] + "c" + n[3] + "))"):
                return True
            if calc("((" + n[0] + "a" + n[1] + ")b" + n[2] + ")c" + n[3]):
                return True
            if calc("(" + n[0] + "a(" + n[1] + "b" + n[2] + "))c" + n[3]):
                return True

        return False
