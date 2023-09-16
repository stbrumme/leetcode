class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : x[0] * 10**6 - x[1]) # sort by w, then h reverse

        heights = [] # store minimum heights
        for w, h in envelopes:
            pos = bisect_left(heights, h)
            if pos == len(heights):
                heights.append(h) # largest so far
            else:
                heights[pos] = h # may overwrite h by itself, too, but often reduces it
                                 # that's where sorting envelopes kicks in

        return len(heights)