class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        while True:
            t = s.replace("01", "10")
            if s == t: # no more changes ?
                return seconds

            # next second
            s = t
            seconds += 1
