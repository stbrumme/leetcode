class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        result  = 0
        longest = 10 # longest forbidden string has 10 letters
        never   = [ set() ] * (longest + 1) # forbidden phrases partitioned by their length
        for f in forbidden:
            never[len(f)].add(f)

        restart = 0 # oldest position where no forbidden string starts

        for i in range(len(word)):
            # look at substrings ending at i, start with length 1
            left = right = i

            # check all possible lengths
            for length in range(1, longest + 1):
                # skip if we already found a forbidden string which is closer
                if left < restart:
                    break

                # restart valid substring if forbidden phrase found
                current = word[left : right + 1]
                if current in never[length]:
                    restart = left + 1
                    break # no need to check other lengths

                left -= 1

            result = max(result, i - restart + 1)

        return result
