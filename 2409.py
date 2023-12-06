class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # brute force
        months = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ] # prepend zero such that months[1] is January

        result = 0
        for m in range(1, 12 + 1):
            for d in range(1, months[m] + 1):
                today = f"{m:02}-{d:02}"

                if today > leaveAlice or today > leaveBob:
                    break

                if arriveAlice <= today <= leaveAlice and arriveBob <= today <= leaveBob:
                    result += 1

        return result
