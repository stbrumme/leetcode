class Solution:
    @cache
    def step(self, s):
        result = ""
        pos   = 1
        count = 1
        while pos < len(s):
            if s[pos] == s[pos - 1]:
                count += 1
            else:
                result += str(count)
                result += s[pos - 1]
                count = 1
            pos += 1

        result += str(count)
        result += s[pos - 1]
        return result


    def countAndSay(self, n: int) -> str:
        s = "1"
        while n > 1:
            s = self.step(s)
            n -= 1
        return s
