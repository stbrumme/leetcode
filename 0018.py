class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # each number should occur at most four times
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        reduced = []
        for f in freq:
            count = min(4, freq[f])
            for _ in range(count):
                reduced.append(f)
        nums = reduced

        # all pairs(i, j) where i < j, grouped by their sum
        two = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i]
                y = nums[j]
                two[x + y].add(tuple([ i, j ]))

        result = set()
        for x in two:
            y = target - x
            if not y in two:
                continue
            if x > y: # optimization, avoid duplicates
                continue

            for tx in two[x]:
                for ty in two[y]:
                    a = tx[0]
                    b = tx[1]
                    c = ty[0]
                    d = ty[1]

                    if a != c and a != d and b != c and b != d: # a<b and c<d are guaranteed
                        four = [ nums[a], nums[b], nums[c], nums[d] ]
                        four.sort()
                        result.add(tuple(four))

        return result
