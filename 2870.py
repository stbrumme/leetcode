class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        result = 0
        for f in freq.values():
            if f == 1:
                return -1

            remain = f % 3
            if   remain == 0:
                # delete in bunches of three
                result += f // 3
            elif remain == 1:
                # delete in bunches of three until 4 identical are left
                # delete the with 2 deletions of two
                result += (f // 3) + 1 # actually (f // 3) - 1) + 2
            else:
                # delete in bunches of three, then the remaining two
                result += (f // 3) + 1 # which is the same as above but for different reasons

        return result
