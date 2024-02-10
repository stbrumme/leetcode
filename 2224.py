class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        result  = 0

        hour1   = int(current[:2])
        minute1 = int(current[3:])
        hour2   = int(correct[:2])
        minute2 = int(correct[3:])

        time1 = hour1 * 60 + minute1
        time2 = hour2 * 60 + minute2

        while time1 % 5 != time2 % 5:
            time1  += 1
            result += 1

        while time1 % 15 != time2 % 15:
            time1  += 5
            result += 1

        while time1 % 60 != time2 % 60:
            time1  += 15
            result += 1

        while time1 != time2:
            time1  += 60
            result += 1

        return result
