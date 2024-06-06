class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        result = []

        changed.sort()
        half = deque() # "normal" values (in contrast to those with twice the value)

        while changed:
            # we already saw a number with twice the value, now there's the normal value
            if half and half[-1] == changed[-1]:
                result.append(half.pop())
                changed.pop()
                continue

            # must be twice the value of something
            high = changed.pop()
            if high & 1:
                return [] # odd number, can't be twice any integer value

            half.appendleft(high >> 1)

        # make sure each doubled value had its counterpart
        return [] if half else result
