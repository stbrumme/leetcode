class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        # prefix sum
        prefix = [ 0 ]
        for n in nums:
            prefix.append(prefix[-1] + n)

        # sum of the k-sized subarray starting here
        here  = [ b - a for a, b in zip(prefix, prefix[k :]) ]

        # maximum sum and its location, scanning from the left side
        left = []
        best = 0
        pos  = 0
        for i in range(len(here)):
            if  best < here[i]:
                best = here[i]
                pos = i

            left.append(( best, pos ))

        # and from the right side
        right = deque()
        best  = 0
        pos   = 0
        for i in reversed(range(len(here))):
            if  best <= here[i]: # small difference: always pick the smaller position if equal
                best  = here[i]
                pos   = i

            right.appendleft(( best, pos ))

        best   = 0
        result = []
        for i in range(k, len(right) - k):
            one, pos1 = left [i - k]
            two, pos2 = right[i + k]
            have = one + here[i] + two
            if  best < have:
                best = have
                result = ( pos1, i, pos2 )

        return result
