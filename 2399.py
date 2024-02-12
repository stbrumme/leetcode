class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        done = [ False ] * 26
        for i, c in enumerate(s):
            value = ord(c) - ord("a")
            if done[value]:
                continue

            done[value] = True

            j = i + distance[value] + 1
            if j >= len(s) or s[j] != c:
                return False

        return True
