class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [ int(s) for s in date.split("-") ]

        # leap years
        length = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ] # no need for December
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            length[1] = 29

        return day + sum(length[i] for i in range(month - 1))
