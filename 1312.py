class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def deeper(left, right):
            if left >= right:
                return 0

            if s[left] == s[right]:
                return deeper(left+1, right-1)

            insertleft  = deeper(left+1, right)
            insertright = deeper(left, right-1)
            return 1 + min(insertleft, insertright)

        return deeper(0, len(s) - 1)