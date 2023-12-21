class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha   = {}
        numeric = {}
        for i in range(26):
            code  = str(i + 1)
            ascii = chr(i + ord("a"))
            alpha[code]    = ascii
            numeric[ascii] = code
        # handle cases such as "10#"
        alpha["0"]   = "_" # placeholder
        numeric["_"] = "0"

        result = []
        for c in s:
            if c == "#":
                two = numeric[result.pop()]
                one = numeric[result.pop()]
                result.append(alpha[one + two])
            else:
                result.append(alpha[c])

        return "".join(result)
