class Solution:
    def compressedString(self, word: str) -> str:
        result = []

        last   = ""
        repeat = 0
        for c in word + "!": # append stop marker to handle last unit properly
            if c == last:
                # same
                repeat += 1
                if repeat == 9:
                    result.append("9" + c)
                    repeat = 0
            else:
                # different
                if repeat > 0:
                    result.append(str(repeat) + last)
                last   = c
                repeat = 1

        return "".join(result)
