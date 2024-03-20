class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        result = 0

        # count letters
        freq = defaultdict(int)
        for w in words:
            for c in w:
                freq[c] += 1

        # group into odd and even
        odd  = 0
        even = 0
        for f in freq.values():
            odd  += f & 1
            even += f - (f & 1)

        # pick shortest words first, try to make palindromes
        for w in sorted(words, key = lambda x : len(x)):
            length = len(w)

            # middle element if odd length
            if length & 1:
                length -= 1
                if odd > 0:
                    odd  -= 1 # preferably pick a letter with odd count
                else:
                    even -= 2 # if not possible, take one with even count
                    odd  += 1

            # another palindrome
            if length <= even:
                even   -= length
                result += 1
            else:
                break

        return result
