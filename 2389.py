class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        for q in queries:
            have   = []
            total  = 0
            length = 0
            for n in nums:
                # collect numbers
                heappush(have, -n)
                total += n
                # but do no exceed the query
                if total > q:
                    total -= -heappop(have) # remove the largest number
                length = max(length, len(have))

            yield length
