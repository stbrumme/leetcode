class Solution:
    def countVowelStrings(self, n: int) -> int:
        # 0 = "a", 1 = "e", 2 = "i", 3 = "o", 4 = "u"
        last = [ 1, 0, 0, 0, 0 ]
        for i in range(n):
            next = [ 0, 0, 0, 0, 0 ]
            for i, l in enumerate(last):
                for j in range(i, 5):
                    next[j] += l
            last = next
        return sum(last)
