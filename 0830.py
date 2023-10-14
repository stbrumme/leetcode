class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pos      = 0
        count    = 0
        previous = ""
        for c in s + "!": # append stop marker to simplify handling of last group
            if c == previous:
                count += 1
            else:
                # new letter
                if count >= 3:
                    yield [ pos - count, pos - 1 ]

                count    = 1
                previous = c

            pos += 1
