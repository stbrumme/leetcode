class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        # same last digit => one element
        if num % 10 == k:
            return 1
        # multiples of ten but last digit isn't zero (would be caught by previous if-clause)
        if k == 0:
            return -1 # impossible

        have = set([ 0 ])
        for step in range(1, num+1):
            next = set()
            for i in range(k, num+1, 10):
                for h in have:
                    if h + i == num:
                        return step
                    if h + i <  num:
                        next.add(h + i)

            have = next
            if not have:
                break

        return -1 # impossible
