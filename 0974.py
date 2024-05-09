class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        total  = 0

        seen    = defaultdict(int)
        seen[0] = 1
        for n in nums:
            total  += n # prefix sum

            modulo  = total % k
            result += seen[modulo]
            seen[modulo] += 1

        return result
