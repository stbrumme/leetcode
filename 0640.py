class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")

        def compute(formula, value): # value should be a string
            # if value == "7": "3+2x" => "3+2*7" => eval
            #                  "3+x"  => "3+*7"  => "3+7" => eval
            formula = formula.replace("x", "*" + value)
            formula = formula.replace("+*", "+")
            formula = formula.replace("-*", "-")
            if formula[0] == "*":
                formula = formula[1 :]

            return eval(formula)

        solution = None
        for i in range(1000):
            for sign in [ -1, +1 ]:
                n = str(i * sign)
                l = compute(left,  n)
                r = compute(right, n)
                if l == r:
                    if solution is not None:
                        return "Infinite solutions"

                    solution = "x=" + n

                # zero has no sign
                if i == 0:
                    break

        return solution if solution is not None else "No solution"
