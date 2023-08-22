class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = defaultdict(int)
        for c in s1:
            freq1[c] += 1

        right = 0
        freq2 = defaultdict(int)
        while right < len(s1):
            freq2[s2[right]] += 1
            right += 1

        left = 0
        while True:
            if freq1 == freq2:
                return True

            if right == len(s2):
                return False

            if freq2[s2[left ]] == 1:
                del freq2[s2[left]]
            else:
                freq2[s2[left ]] -= 1

            freq2[s2[right]] += 1
            left  += 1
            right += 1

        return False
