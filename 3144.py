class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        # convert to 0...25
        nums = [ ord(c) - ord("a") for c in s ]
        size = len(nums)

        @cache
        def deeper(pos):
            if pos >= size:
                return 0

            have = [ 0 ] * 26
            have[nums[pos]] += 1

            # all strings with one or two characters are always balanced
            best = 1 + deeper(pos + 1)

            for i in range(pos + 1, size):
                have[nums[i]] += 1

                okay = True
                need = max(have)
                for h in have:
                    if h > 0 and h != need:
                        okay = False
                        break

                if okay:
                    best = min(best, 1 + deeper(i + 1))
            return best

        return deeper(0)
