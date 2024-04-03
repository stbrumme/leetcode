class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # build blocks of consecutive letters, count them, too
        consecutive = []
        freq = defaultdict(int)
        for c in text:
            freq[c] += 1
            if consecutive and c == consecutive[-1][0]:
                consecutive[-1][1] += 1
            else:
                consecutive.append([ c, 1 ])

        # find longest block
        result = 0
        for x in consecutive:
            length = x[1]
            # append an available letter (by swapping)
            if freq[x[0]] > length:
                length += 1
            result = max(result, length)

        # merge two blocks if separated by a single letter
        for left, middle, right in zip(consecutive, consecutive[1 :], consecutive[2 :]):
            if middle[1] == 1 and left[0] == right[0]:
                # try to find a spare letter to replace "middle"
                # if it isn't there, replace "middle" by the last letter of "right"
                length = min(left[1] + right[1] + 1, freq[left[0]]) # the latter will be left[1] + right[1]
                result = max(result, length)

        return result
