class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        result = 0

        # important constraint: "each person is contained in exactly one pair"

        good = {}
        for x, y in pairs:
            # better friends (those who might be potentially unhappy)
            better  = preferences[x].index(y)
            good[x] = preferences[x][ : better]

            # and the other way 'round
            better  = preferences[y].index(x)
            good[y] = preferences[y][ : better]

        # check inverse relation
        for x in good:
            for y in good[x]:
                if x in good[y]:
                    result += 1
                    break

        return result
