class Solution:
    def smallestString(self, s: str) -> str:
        result = ""

        rotate = False # cycle characters
        aaa    = True  # True as long as all initial characters are "a"
        for c in s:
            # change state
            if c == "a":
                if rotate: # speed optimization: copy unchanged final characters
                    need = len(s) - len(result)
                    result += s[-need :]
                    break

                rotate = False
            else:
                if aaa:
                    rotate = True
                    aaa    = False

            # copy or cycle
            if rotate:
                result += chr(ord(c) - 1)
            else:
                result += c

        # string is "aaa...aaa"
        if aaa:
            # replace final "a" by "z"
            result = result[ : -1] + "z"

        return result
