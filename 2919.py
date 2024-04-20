class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        # just needs to work for all subarrays with size 3
        # because then it works for all larger subarrays as well

        three = two = one = best = 0
        for n in nums:
            # just consider current element
            need = k - n
            if need < 0:
                need = 0 # always increment, never decrement

            # "shift"
            three = two
            two   = one
            one   = need + best

            # prefer the least number of imcrements
            best = min(one, two, three)

        return best
