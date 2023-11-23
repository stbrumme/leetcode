class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # score[i] contains the score for range (0, i)
        score = [ 0 ] * len(nums)
        # each jump sequence contains the first field (and the last field)
        score[0] = nums[0]
        # most recent jump indices in descending order of their score
        candidates = [ 0 ] # candidates[0] is the best
        for i in range(1, len(nums)):
            # remove outdated source fields
            threshold = i - k
            if candidates[0] < threshold:
                candidates.pop(0)

            # choose best source field plus current field
            current = score[candidates[0]] + nums[i]
            # remove worse jumps
            while candidates and score[candidates[-1]] < current:
                candidates.pop()

            score[i] = current
            candidates.append(i)

        return score[-1]
