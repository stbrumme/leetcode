class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # let's try it without Longest Common Sequence algorithm
        # which requires quite a significant amount of memory (len(nums1) * len(nums2)

        result = 0

        def fnv(hash_, value):
            # FNV hash, 32 bit
            return ((hash_ ^ value) * 16777619) & 0xFFFFFFFF

        hash1 = nums1.copy()
        hash2 = nums2.copy()

        x = 0

        size = min(len(nums1), len(nums2))
        for length in range(1, size + 1):
            shared = set(hash1) & set(hash2)
            if not shared:
                break

            # exclude hash collisions
            found = False
            for i, h1 in enumerate(hash1):
                if h1 in shared:
                    for j, h2 in enumerate(hash2):
                        if h2 == h1:
                            x += 1
                            if nums1[i : i + length] == nums2[j : j + length]:
                                found = True
                                result = length
                                break
                    # no collision, match was verified
                    if found:
                        break

            # no matching strings
            if not found:
                break

            # update hashes
            hash1.pop()
            hash2.pop()
            for i in range(len(nums1) - length):
                hash1[i] = fnv(hash1[i], nums1[i + length])
            for i in range(len(nums2) - length):
                hash2[i] = fnv(hash2[i], nums2[i + length])

        return result
