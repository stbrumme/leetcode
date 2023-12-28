class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        result = ""

        # faster lookup
        lookup = { key: value for key, value in knowledge }

        inside = False
        key    = ""
        for c in s:
            # start of key
            if c == "(":
                inside = True
                key    = ""
                continue

            # end of key
            if c == ")":
                inside  = False
                result += lookup.get(key, "?")
                continue

            if inside:
                key    += c # key's name
            else:
                result += c # ordinary text

        return result
