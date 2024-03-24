class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def deeper(pos, formula, leadingZero):
            if pos == len(num):
                if eval(formula) == target:
                    result.append(formula)
                return

            digit = num[pos]
            if not leadingZero:
                deeper(pos + 1, formula + digit, False)

            deeper(pos + 1, formula + "+" + digit, digit == "0")
            deeper(pos + 1, formula + "-" + digit, digit == "0")
            deeper(pos + 1, formula + "*" + digit, digit == "0")

        deeper(1, num[0], num[0] == "0")
        return result
