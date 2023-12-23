class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        for type, color, name in items:
            if   ruleKey == "type"  and type  == ruleValue:
                result += 1
            elif ruleKey == "color" and color == ruleValue:
                result += 1
            elif ruleKey == "name"  and name  == ruleValue:
                result += 1
        return result
