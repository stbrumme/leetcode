class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # rotate each cuboid such that width <= length <= height
        for c in cuboids:
            c.sort()
        # sort all cuboids by their width (and length/height if same width)
        cuboids.sort()

        @cache
        def deeper(i): # stack cuboids from 0 to i, return their height
            result  = 0

            current = cuboids[i]
            for j in range(i):
                other = cuboids[j]
                if other[1] <= current[1] and other[2] <= current[2]: # always other[0] <= current[0]
                    # stack both
                    result = max(result, deeper(j))

            # add current cuboid's height, too
            return result + current[2]

        return max([ deeper(i) for i in range(len(cuboids)) ])
