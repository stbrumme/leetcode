class RangeModule:
    def __init__(self):
        self.start = [] # sorted list [ left ]
        self.end   = [] # sorted list [ right ]

    def addRange(self, left: int, right: int) -> None:
        if not self.start:
            self.start = [ left ]
            self.end   = [ right ]
            return

        pos  = bisect_left(self.start, left)
        pos  = max(0, pos - 4) # crude heuristic

        low  = pos             # strictly smaller
        high = len(self.start) # strictly larger

        start = left
        end   = right

        for i in range(pos, len(self.start)):
            l = self.start[i]
            r = self.end  [i]

            if   r < left:
                low  = i + 1
            elif l > right:
                high = i
                break
            else:
                # merge overlapping, may happen several times
                start = min(start, l)
                end   = max(end,   r)

        self.start[low : high] = [ start ]
        self.end  [low : high] = [ end ]

    def queryRange(self, left: int, right: int) -> bool:
        pos = bisect_left(self.start, left)

        if pos < len(self.start):
            # an interval starts at "left" ?
            l = self.start[pos]
            r = self.end  [pos]
            if l == left and right <= r:
                return True

        # must check previous interval
        pos -= 1
        if pos < 0:
            return False
        l = self.start[pos]
        r = self.end  [pos]
        return l <= left and right <= r

    def removeRange(self, left: int, right: int) -> None:
        # similar to addRange
        pos  = bisect_left(self.start, left)
        pos  = max(0, pos - 4) # crude heuristic

        low  = pos             # strictly smaller
        high = len(self.start) # strictly larger

        # split
        start = []
        end   = []

        for i in range(pos, len(self.start)):
            l = self.start[i]
            r = self.end  [i]

            if   r <= left:
                low  = i + 1
            elif l >= right:
                high = i
                break
            else:
                # split or completely remove
                if l < left:  # we know that r > left
                    start.append(l)
                    end  .append(left)
                if r > right: # we know that l < right
                    start.append(right)
                    end  .append(r)
                # careful: NOT elif instead of if, an existing interval might be split in half

        self.start[low : high] = start
        self.end  [low : high] = end
