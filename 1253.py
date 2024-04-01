class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []

        one = []
        two = []
        for c in colsum:
            if   c == 0:
                one.append(0)
                two.append(0)
            elif c == 2:
                one.append(1)
                two.append(1)
                upper -= 1
                lower -= 1
            else: # c == 1
                if upper >= lower:
                    one.append(1)
                    two.append(0)
                    upper -= 1
                else:
                    one.append(0)
                    two.append(1)
                    lower -= 1

        return [ one, two ] if upper == 0 and lower == 0 else []
