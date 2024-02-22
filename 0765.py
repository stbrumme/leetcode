class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        result = 0

        # seats of each person
        seat = { who : where for where, who in enumerate(row) }

        for i in range(0, len(row), 2):
            a = row[i]
            b = row[i + 1]

            # true love of a => flip lowest bit
            love = a ^ 1
            if b != love:
                # push b away ;-) and replace by true love
                row[seat[love]] = b
                seat[b] = seat[love]
                result += 1
                # actually I don't update row[i + 1] and seat[love] because it isn't needed

        return result
