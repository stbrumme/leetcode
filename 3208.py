class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        result = 0
        size   = len(colors)

        # length of alternating group at previous position
        previous = 1
        # and at current position
        current  = 0

        # I use two loops and an if to avoid slow modulo and keep memory consumption low
        # the inner part of each loop (and the if) is almost identical

        # same cycle
        for a, b in zip(colors, colors[1 : ]):
            current  = (a != b) * previous + 1 # same as 1 if a == b else previous + 1
            result  += current >= k
            previous = current

        # wraparound
        if k >= 1:
            current  = 1 if colors[ 0 ] == colors[   -1  ] else previous + 1
            result  += current >= k
            previous = current

        # second cycle
        for a, b in zip(colors, colors[1 : k - 1]):
            current  = (a != b) * previous + 1
            result  += current >= k
            previous = current

        return result
