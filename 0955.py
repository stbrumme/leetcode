class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        length  = len(strs[0])
        size    = len(strs)

        result  = 0
        ordered = [ "" ] * size
        for i in range(length):
            # add a letter
            for j in range(size):
                ordered[j] += strs[j][i]

            ok = all(ordered[k - 1] <= ordered[k] for k in range(1, size))
            if not ok:
                # delete that letter
                result += 1
                for j in range(size):
                    ordered[j] = ordered[j][:-1]

        return result
