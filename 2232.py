class Solution:
    def minimizeResult(self, expression: str) -> str:
        low    = float("inf")
        result = ""
        left, right = expression.split("+")
        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                formula = left[:i] + "*(" + left[i:] + "+" + right[:j] + ")*" + right[j:]
                current = eval(formula.strip("*")) # no trailing/leading *
                if low > current:
                    low = current
                    result = formula.replace("*", "") # judge wants without *

        return result
