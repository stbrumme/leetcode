class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a = ord("a")
        # count letters
        freq1 = [ 0 ] * 26
        for c in word1:
            freq1[ord(c) - a] += 1

        freq2 = [ 0 ] * 26
        for c in word2:
            freq2[ord(c) - a] += 1

        # count distinct letters
        def distinct(freq):
            return sum(1 for f in freq if f > 0)

        # early exit
        diff = abs(distinct(freq1) - distinct(freq2))
        if diff > 2:
            return False # a single swap can fix at most 2 differences

        for one in range(len(freq1)):
            if freq1[one] == 0:
                continue

            for two in range(len(freq1)):
                if freq2[two] == 0:
                    continue

                # pretty much brute force:
                # modify histograms based on the swap, then check and undo
                freq1[one] -= 1
                freq1[two] += 1
                freq2[one] += 1
                freq2[two] -= 1

                # and check the number of unique characters
                if distinct(freq1) == distinct(freq2):
                    return True

                # undo changes
                freq1[one] += 1
                freq1[two] -= 1
                freq2[one] -= 1
                freq2[two] += 1

        return False
