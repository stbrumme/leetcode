class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        size = len(s)

        # count optimal partitions
        @cache
        def deeper(pos):
            # end of string, no more partitions needed
            if pos == size:
                return 0

            best = +inf
            have = 0
            for i in range(pos, size):
                # add one digit
                have *= 10
                have += int(s[i])
                # too big ?
                if have > k:
                    break

                # next partition
                best = min(best, deeper(i + 1))

            return best + 1 # insert a partition

        result = deeper(0)
        return result if result != +inf else -1
