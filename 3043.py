class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0

        # mix all numbers, keep track where they come from
        all = []
        for a in arr1:
            all.append(( str(a), 1 ))
        for b in arr2:
            all.append(( str(b), 2 ))
        all.sort()

        for left, right in zip(all, all[1 :]):
            one, src1 = left
            two, src2 = right
            if src1 != src2:
                # find common prefix
                i = 0
                for a, b in zip(one, two):
                    if a == b:
                        i += 1
                    else:
                        break

                result = max(result, i)

        return result
