class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = 0
        current = -1001

        again = True
        while again:
            next = +1001
            again = False

            for p in pairs:
                if p[0] > current and p[1] < next:
                    next = p[1]
                    again = True

            if again:
                current = next
                length += 1

        return length
