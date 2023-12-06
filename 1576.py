class Solution:
    def modifyString(self, s: str) -> str:
        result = []
        for i, c in enumerate(s):
            # keep normal characters
            if c != "?":
                result.append(c)
                continue

            # "neighbors"
            prev = "" if i == 0          else result[-1]
            next = "" if i == len(s) - 1 else s[i + 1]

            # three candidates are sufficient to handle all situtations
            replace = [ "a", "b", "c" ]
            for r in replace:
                if prev != r and next != r:
                    result.append(r)
                    break

        return "".join(result)
