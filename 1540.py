class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        # count shifts between s[i] and t[i]
        steps = [ 0 ] * 26
        for one, two in zip(s, t):
            # no shift
            if one == two:
                continue

            one = ord(one)
            two = ord(two)
            if two < one:
                two += 26 # wraparound

            shift = two - one
            if steps[shift] == 0:
                steps[shift]  = shift # first time we observe that shift
            else:
                steps[shift] += 26    # that shift was already seen, need to wait a full cycle

            if steps[shift] > k:
                return False

        return True
