class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = expression.replace("f", "0")
        expression = expression.replace("t", "1")
        expression = expression.replace("!", "1-")
        expression = expression.replace("&(", "min(1,")
        expression = expression.replace("|(", "max(0,")
        return eval(expression) == 1
