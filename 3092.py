class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        high = [] # max-heap
        have = defaultdict(int) # current amount of IDs
        for n, f in zip(nums, freq):
            # Python supports only min-heaps, therefore perform all operations on negated freq
            f = -f

            have[n] += f
            heappush(high, ( have[n], n ))

            # remove invalid entries from heap
            while high:
                count, id = high[0]
                if count == have[id]:
                    break
                heappop(high)

            yield -high[0][0] # remember we inversed freq
