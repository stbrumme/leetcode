class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        s = str(num)
        for i in range(len(s) - k + 1):
            sub = int(s[i : i + k])
            if sub > 0 and num % sub == 0:
                result += 1
        return result
