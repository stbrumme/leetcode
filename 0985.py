class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(n for n in nums if n % 2 == 0)
        for q in queries:
            if nums[q[1]] % 2 == 0:
                s -= nums[q[1]]

            nums[q[1]] += q[0]

            if nums[q[1]] % 2 == 0:
                s += nums[q[1]]

            yield s