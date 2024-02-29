class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = [ label ]
        if label == 1:
            return result

        # compute highest and lowest value for each row
        high = low = row = 1
        rows = [ [ 1, 1 ] ] # first row
        while high < label:
            high = 2 * high + 1
            low  = 2 * low
            rows.append ([ low, high ])

        # process rows bottom-up
        while label > 1:
            low, high = rows.pop()
            l2, h2    = rows[-1]      # peek to level above

            if len(rows) & 1:
                pos   = label - low   # left-to-right
                label = h2 - pos // 2 # right-to-left
            else:
                pos   = high - label  # right-to-left
                label = l2 + pos // 2 # left-to-right

            result.append(label)

        return reversed(result) # restore original order
