class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        # arrays are 1-based in this problem, whereaus Python/C/Java/... prefer 0-based indices
        size = len(nums)

        def possible(when):
            # last timestamp when each index can be marked
            mark = [ -1 ] * size
            for i, c in enumerate(changeIndices[ : when]):
                c -= 1 # 1- to 0-based
                mark[c] = i

            steps = 0
            for i, c in enumerate(changeIndices[ : when]):
                c -= 1 # 1- to 0-based

                # final opportunity to mark
                if i == mark[c]:
                    # apply decrements
                    steps  -= nums[c]
                    mark[c] = 0
                    if steps < 0:
                        return False # not enough decrements
                else:
                    steps += 1

            return sum(mark) == 0 # all are done (= 0)

        # each number needs to be decremented to zero plus one step to be marked
        need = sum(nums) + size
        # last possible timestamp
        last = len(changeIndices) + 1

        # earliest timestamp where each number can be marked
        seen = set()
        for i, c in enumerate(changeIndices):
            seen.add(c)
            if len(seen) == size:
                need = max(need, i)
                break

        result = need + bisect_left(range(need, last + 1), True, key = possible)
        return result if result <= last else -1
