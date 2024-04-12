class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        result = 0
        size   = len(nums)

        # sort data such that collisions are found early
        reject = defaultdict(int)
        for n1 in nums:
            for n2 in nums:
                reject[n1] += abs(n1 - n2) == k
        nums.sort(key = lambda x : -reject[x])

        def deeper(pos, have): # have is a bitmask of used elements of "nums"
            # all elements visited, beautiful subset found
            if pos == size:
                nonlocal result
                result += have > 0 # ignore empty set
                return

            # skip nums[pos]
            deeper(pos + 1, have)

            # use it, but check first if still beautiful
            ugly = False
            for i in range(pos):
                mask = 1 << i
                if mask & have:
                    if abs(nums[pos] - nums[i]) == k:
                        ugly = True
                        break

            if not ugly:
                deeper(pos + 1, have | (1 << pos))

        deeper(0, 0)
        return result
