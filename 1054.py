class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = defaultdict(int)
        for b in barcodes:
            freq[b] += 1

        # max-heap
        next = []
        for f in freq:
            heappush(next, (-freq[f], f)) # negate => max instead of min-heap

        result = [ None ] # placeholder
        while len(next) >= 2:
            # choose most frequent or second most frequent
            one = heappop(next)
            two = heappop(next)

            if result[-1] == one[1]:
                two = (two[0] + 1, two[1]) # remember: inverted sign
                result.append(two[1])
            else:
                one = (one[0] + 1, one[1])
                result.append(one[1])

            if one[0] != 0:
                heappush(next, one)
            if two[0] != 0:
                heappush(next, two)

        return result[1:] + [ next[0][1] ] # remove placeholder, add last barcode
