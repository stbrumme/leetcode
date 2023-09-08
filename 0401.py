class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # just brute-force it, no smart bit rearrangement
        for hour in range(12):
            for minute in range(60):
                if hour.bit_count() + minute.bit_count() == turnedOn:
                    yield f"{hour}:{minute:02d}"
