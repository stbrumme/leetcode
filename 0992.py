class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # find left-most sliding window which is a good subarray
        left = right = 0
        freq = defaultdict(int)
        while len(freq) < k and right < len(nums):
            freq[nums[right]] += 1
            right += 1

        # no good subarrays at all
        if len(freq) < k:
            return 0

        # slowly slide to the right
        result = 0
        while True:
            current = freq.copy()
            # reduce subarray until we lose a unique integer
            for scan in range(left, right):
                result += 1

                slideout = nums[scan]
                current[slideout] -= 1
                if current[slideout] == 0:
                    break

            # we're done
            if right == len(nums):
                break

            # slide right by one
            freq[nums[right]] += 1
            right += 1

            # adjust left side until we have a good array
            while len(freq) > k:
                slideout = nums[left]
                if freq[slideout] > 1:
                    freq[slideout] -= 1
                else:
                    del freq[slideout]
                left += 1

        return result
