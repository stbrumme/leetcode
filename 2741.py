class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        modulo = 1_000_000_007

        follow = defaultdict(list)
        for n in nums:
            for i, other in enumerate(nums):
                if n % other == 0 or other % n == 0:
                    follow[n].append((1 << i, other))

        todo = {} # bitmask of processed indices, previous number

        # first number
        for i, n in enumerate(nums):
            todo[ ( 1 << i, n ) ] = 1

        # all other numbers
        size = len(nums)
        for _ in range(size - 1):
            next = defaultdict(int)

            for ( done, prev ), count in todo.items():
                for mask, n in follow[prev]:
                    # ... but not if already done so in earlier steps
                    if not (done & mask):
                        # current pair or last pair need to be special
                        if n % prev == 0 or prev % n == 0:
                            next[( done | mask, n )] += count

            todo = next

        return sum(todo.values()) % modulo
