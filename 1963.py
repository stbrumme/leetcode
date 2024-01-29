class Solution:
    def minSwaps(self, s: str) -> int:
        result = 0

        open = 0
        for c in s:
            if c == "[":
                open += 1
            else:
                open = max(0, open - 1) # never negative

        # some "]" may be found before their parter "[" is seen
        # each "]]..[[" can be resolved with a single swap
        # =>   "[]..[]" (first and last character)
        # if "open" is an odd number then just swap its "[" and "]"
        return (open // 2) + (open & 1)
