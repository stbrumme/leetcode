class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        cookie = 0
        for greed in g:
            while cookie < len(s) and greed > s[cookie]:
                cookie += 1
            if cookie < len(s):
                result += 1
            cookie += 1

        return result
