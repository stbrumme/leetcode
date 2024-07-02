class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result = 0

        delta  = defaultdict(int)
        for start, end in meetings:
            if start <= days:
                delta[start  ] += 1
                delta[end + 1] -= 1

        delta[days + 1] += 0

        last = 1     # most recently processed day
        meetings = 0 # number of ongoing meetings
        for today, change in sorted(delta.items()):
            # no meeting
            if meetings == 0:
                result += today - last

            meetings += change

            last = today
            if last > days: # early exit
                break

        return result
