class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        result = -1

        left  = {} # left  end of all groups and their length
        right = {} # right end of all groups and their length
        sizes = defaultdict(int)

        for i, a in enumerate(arr):
            # new group
            left [a]  = 1
            right[a]  = 1
            sizes[1] += 1

            # merge two groups, parameters refer to their start (= left[])
            def merge(one, two): # one < two
                # combine
                length = left[one] + left[two]
                last   = one + length - 1
                left[one] = right[last] = length
                sizes[length] += 1

                # clean up
                sizes[left [two    ]] -= 1
                sizes[right[two - 1]] -= 1
                del   left [two    ]
                del   right[two - 1]

            if a + 1 in left:
                merge(a, a + 1)
            if a - 1 in right:
                merge(a - right[a - 1], a)

            # check if a group exists
            if sizes[m] > 0:
                result = i + 1

        return result
