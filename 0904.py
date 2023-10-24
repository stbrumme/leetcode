class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        result = streak = 2 # always possible to pick from the first two trees
        a      = fruits[0]
        b      = fruits[1]
        prev   = b
        repeat = 1
        for f in fruits[2:]:
            if f == a or f == b or a == b:
                # keep picking
                streak += 1
                if a == b:
                    a = f
            else:
                # start new streak
                result = max(result, streak)
                streak = 1 + repeat # first two trees of every streak are valid
                a = prev
                b = f

            if prev == f:
                repeat += 1
            else:
                prev   = f
                repeat = 1

        return max(result, streak) # maybe best streak ended on the final tree
