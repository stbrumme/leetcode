class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")

        # strip st/nd/rd/th
        day = int(day[:-2])

        # convert names
        lookup = [ "", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
        month  = lookup.index(month)

        # year is unchanged, day and month need a leading zero
        return f"{year}-{month:02d}-{day:02d}"
