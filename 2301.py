class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        # a character may map to multiple other characters
        convert = set() # strings of size 2: "xy" means "x" can map to "y"
        for old, new in mappings:
            convert.add(old + new)

        for i in range(len(s)):
            same = 0
            for a, b in zip(sub, s[i :]):
                if a == b or a + b in convert:
                    same += 1
                else:
                    same  = 0
                    break

            if same == len(sub):
                return True

        return False
