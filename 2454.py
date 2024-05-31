class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        result = [ -1 ] * len(nums)

        # two min-heaps
        one = []
        two = []
        for i, n in enumerate(nums):
            # second greater
            while two and two[0][0] < n:
                _, pos = heappop(two)
                result[pos] = n

            # move first greater to second greater
            while one and one[0][0] < n:
                heappush(two, heappop(one))

            heappush(one, ( n, i ))

        return result
