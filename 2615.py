class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        size   = len(nums)
        result = [ None ] * size

        pos = defaultdict(list)
        for i, n in enumerate(nums):
            pos[n].append(i)

        for p in pos:
            same  = pos[p]
            size  = len(same)

            left  = 0
            right = sum(same) - size * same[0]
            same += [ +inf ]
            for i, (s, next) in enumerate(zip(same, same[1 :]), 1):
                result[s] = left + right

                gap       = next - s
                left     += gap * i
                right    -= gap * (size - i)

        return result
