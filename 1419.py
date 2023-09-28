class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        result = 0

        # c,r,o,a,k are all different characters
        pos   = { "c" : 0, "r" : 1, "o" : 2, "a" : 3, "k" : 4 }
        count = [ 0 ] * 5
        for c in croakOfFrogs:
            # invalid language
            if c not in pos:
                return -1

            count[pos[c]] += 1

            # invalid order
            for i in range(1, 5):
                if count[i - 1] < count[i]:
                    return -1

            # simultaneous croaks
            result = max(result, count[0] - count[4])

        return result if count[0] == count[4] else -1 # unfinished croaks
