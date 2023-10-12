class Solution:
    def maximumTime(self, time: str) -> str:
        # pretty much brute-force
        regex = time.replace("?", ".")
        for hour in range(23, -1, -1):
            # match hour
            s = f"{hour:02d}"
            if not re.search(regex[:2], s):
                continue

            # match minute
            for minute in range(59, -1, -1):
                s = f"{hour:02d}:{minute:02d}"
                if re.search(regex, s):
                    return s
