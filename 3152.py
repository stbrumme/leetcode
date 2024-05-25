class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # prefix sum of parity n + position
        prefix = [ 0 ]
        for i, n in enumerate(nums):
            prefix.append(prefix[-1] + ((n + i) & 1)) # less sneaky (n ^ i) & 1

        for a, b in queries:
            # parity must be always 0 or always 1
            parity = prefix[b + 1] - prefix[a]
            length =        b + 1  -        a
            yield parity == 0 or parity == length
