class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for d in details:
            age = int(d[11 : 13])
            result += 1 if age > 60 else 0
        return result
