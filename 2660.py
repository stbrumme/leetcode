class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(turns):
            result = 0
            for i, t in enumerate(turns):
                result += t
                if   i >= 1 and turns[i - 1] == 10:
                    result += t
                elif i >= 2 and turns[i - 2] == 10:
                    result += t
            return result

        one = score(player1)
        two = score(player2)
        if one > two:
            return 1
        if one < two:
            return 2
        return 0
