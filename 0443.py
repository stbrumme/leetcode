class Solution:
    def compress(self, chars: List[str]) -> int:
        groups = []
        last = ""
        for c in chars:
            if c == last:
                groups[-1].append(c)
            else:
                groups.append([ c ])
                last = c

        pos = 0
        for g in groups:
            chars[pos] = g[0]
            pos += 1
            if len(g) > 1:
                for c in str(len(g)):
                    chars[pos] = c
                    pos += 1

        while len(chars) > pos:
            del chars[-1]

        return pos
