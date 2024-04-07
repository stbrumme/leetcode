class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # actually used bits
        high = max(nums)
        bits = 1
        while (1 << bits) - 1 < high:
            bits += 1

        need = defaultdict(list) # indexes where this bit isn't set
        last = []                # last index which set a bit
        have = []                # already set bits
        for i, n in enumerate(nums):
            have.append(n)
            last.append(i)

            for bit in range(bits):
                mask = 1 << bit
                if n & mask:
                    # longer subarrays
                    for x in need[bit]:
                        # double check
                        if (have[x] | n) != have[x]:
                            last[x]  = i
                            have[x] |= n
                    need[bit].clear()
                else:
                    # these bits could be ORed
                    need[bit].append(i)

        # distance to last change
        return [ l - i + 1 for i, l in enumerate(last) ]
