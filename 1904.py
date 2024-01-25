class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def normalize(when, roundUp): # convert time to an integer/unit, one hour equals 4 units
            hour, minute = when.split(":")
            hour   = int(hour)
            minute = int(minute)
            if roundUp:
                minute += 14
            return 4 * hour + minute // 15

        start = normalize(loginTime,  True)
        stop  = normalize(logoutTime, False)

        if loginTime < logoutTime:
            return max(0,   stop - start)
        else:
            return 24 * 4 + stop - start
