class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # datetime needs to be there twice
        one  = datetime.datetime.strptime(max(date1, date2), "%Y-%m-%d")
        two  = datetime.datetime.strptime(min(date1, date2), "%Y-%m-%d")
        return (one - two).days
