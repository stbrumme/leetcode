class Solution:
    @cache
    def deeper(self, s, have, dots):
        if dots == 3:
            # final part
            if not s:
                return
            if s[0] == "0" and len(s) > 1:
                return
            if int(s) > 255:
                return
            self.result.append(have + s)
            return

        if not s:
            return

        # performance
        need = 4 - dots
        if need*3 < len(s):
            return

        # no leading zeros
        if s[0] == "0":
            self.deeper(s[1:], have + s[:1] + ".", dots + 1)
            return

        # 1,2 or 3 digits
        for i in range(1, 4):
            if i == 3:
                if int(s[:i]) > 255:
                    break
            self.deeper(s[i:], have + s[:i] + ".", dots + 1)


    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.deeper(s, "", 0)
        return self.result
