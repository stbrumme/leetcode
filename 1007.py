class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = +inf

        # brute force: expect each number to be in the top or bottom row
        for need in ( 1,2,3,4,5,6 ):
            for g in [ zip(tops, bottoms), zip(bottoms, tops) ]:
                okay  = True
                swaps = 0
                for one, two in g:
                    # try to rotate
                    if one != need:
                        if two == need and swaps < result:
                            swaps += 1
                        else:
                            okay = False
                            break

                # valid sequence
                if okay:
                    result = swaps

        return result if result != +inf else -1
