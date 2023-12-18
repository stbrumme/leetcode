class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # strings without any brackets
        if s[0] != "[":
            return NestedInteger(int(s))

        deeper = []
        num    = "" # current numeric sequence
        for c in s:
            if   c in "-0123456789":
                num += c
            elif c == "[":
                deeper.append(NestedInteger())
            else: # "," or "]"
                if num:
                    deeper[-1].add(NestedInteger(int(num)))
                    num = ""

                if c == "]":
                    # merge with parent
                    nested = deeper.pop()
                    if not deeper:
                        return nested # final bracket
                    deeper[-1].add(nested)
