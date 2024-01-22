class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [ ( a, s ) for a, s in zip(ages, scores) ]
        players.sort(reverse = True) # oldest first, prefer higher score if same age

        @cache
        def deeper(i): # return team score if i is the lowest scoring player (and youngest)
            younger, lowscore = players[i]
            result = lowscore # new team with a single player

            for j in range(i):
                # check against all teams where all members have higher score
                # (they must be older or at least same age)
                older, highscore = players[j]
                if highscore >= lowscore:
                    result = max(result, lowscore + deeper(j)) # join team

            return result

        return max(deeper(i) for i in range(len(players)))
