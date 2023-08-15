class Solution:
    def maximumSwap(self, num: int) -> int:
        # brute-force
        if num < 10:
            return num

        result = num

        s = str(num)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                current = int(s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:])
                if result < current:
                    result = current

        return result
