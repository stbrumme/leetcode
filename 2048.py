class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        candidates = [ "1", "22", "333", "4444", "55555", "666666",
                       "122", "1333", "14444", "155555",
                       "22333", "224444",
                       "122333" ]
        result = 1224444 # smallest such number above 10**6
        for c in candidates:
            for p in set(permutations(c)):
                i = int("".join(p))
                if n < i < result:
                    result = i

        return result