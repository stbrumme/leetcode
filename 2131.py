class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        one  = defaultdict(int) # count words whose letters are     in alphabetical order
        two  = defaultdict(int) # count words whose letters are not in alphabetical order
        same = defaultdict(int) # count words whose letters are     identical

        for w in words:
            if   w[0] == w[1]:
                same[w] += 1
            elif w[0] <  w[1]:
                one [w] += 1
            else:
                two [w] += 1

        result = 0
        # build left and right side
        for o in one:
            # find partner
            t = o[::-1]
            result += 4 * min(one[o], two[t]) # 2 words with 2 letters each

        # add middle
        middle = 0
        for s in same:
            # if multiple words with same letter exist, they can be added to the left and right side
            result += 4 * (same[s] // 2)
            # and at most one such word is placed in the middle
            if middle == 0 and same[s] & 1:
                middle = 2

        return result + middle
