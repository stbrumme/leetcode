class Solution:
    def explode(self, s):
        parts = s.split(".")
        return [int(x) for x in parts]

    def compareVersion(self, version1: str, version2: str) -> int:
        a = self.explode(version1)
        b = self.explode(version2)

        while len(a) < len(b):
            a.append(0)
        while len(b) < len(a):
            b.append(0)

        for i in range(len(a)):
            if a[i] < b[i]:
                return -1
            if a[i] > b[i]:
                return +1

        return 0
