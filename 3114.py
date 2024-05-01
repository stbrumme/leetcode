class Solution:
    def findLatestTime(self, s: str) -> str:
        hours = s[0]
        if s[0] == "?":
            hours = "1" if s[1] in "01?" else "0"
        hours += min("9", s[1])
        hours  = min(hours, "11") # handle overflow

        minutes  = "5" if s[3] == "?" else s[3]
        minutes += min("9", s[4])

        return hours + ":" + minutes
