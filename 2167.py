class Solution:
    def minimumTime(self, s: str) -> int:
        size   = len(s)
        result = size

        # index of each illegal car
        illegal = [ i for i, c in enumerate(s) if c == "1" ]
        # edge cases
        if not illegal:
            return 0
        if len(illegal) == size:
            return size

        # cost to remove all cars if using the left side only
        left = []
        for i in illegal:
            step1 = i + 1                       # remove all cars
            step3 = left[-1] + 2 if left else 2 # remove a single car
            left.append(min(step1, step3))      # select optimal choice

        # cost to remove all cars if using the right side, combine with left side
        right = 0
        for i in reversed(illegal):
            result = min(result, left.pop() + right)
            # update right side
            step2  = size - i                   # remove all cars
            step3  = right + 2                  # remove a single car
            right  = min(step2, step3)          # select optimal choice
        result = min(result, right)             # only from right side

        return result
