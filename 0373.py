class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        all = defaultdict(list)

        threshold = 10**11
        for i in nums1:
            if (i + nums2[0] > threshold):
                break

            for j in nums2:
                if i+j > threshold:
                    break
                all[i+j].append([i, j])

            sums = sorted(all.keys())

            size = 0
            keep = True
            for j in sums:
                size += len(all[j])
                if keep and size >= k:
                    threshold = j
                    keep = False
                    continue

                if not keep:
                    del all[j]

        sums = sorted(all.keys())
        result = []
        found = 0
        for i in sums:
            for j in all[i]:
                if found == k:
                    break

                result.append(j)
                found += 1

        return result
