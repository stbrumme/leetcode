class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        last   = [] # smallest last element for sequences of length n
                    # last[n+1] will always be >= than last[n]
        for o in obstacles:
            pos = bisect_right(last, o)
            yield pos + 1      # one-based results
            if pos == len(last):
                last.append(o) # an even longer sequence
            else:
                last[pos] = o  # lower last element