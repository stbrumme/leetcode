class Solution:
    def countTime(self, time: str) -> int:
        # once again: brute force
        regex = time.replace("?", ".")
        matches = 0
        for hour in range(24):
            for minute in range(60):
                timestamp = f"{hour:02d}:{minute:02d}"
                if re.search(regex, timestamp):
                    matches += 1
        return matches
