class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        result = 0

        all = defaultdict(dict)
        for player, color in pick:
            all[player][color] = all[player].get(color, 0) + 1

        for player in all:
            if max(all[player].values()) > player:
                result += 1

        return result
