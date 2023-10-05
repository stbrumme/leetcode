class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def sign(x):
            return +1 if x > 0 else -1

        size  = len(nums)
        todo  = set() # reference another node
        final = set() # self-loops
        for i, n in enumerate(nums):
            if n % size == 0:
                final.add(i)
            else:
                todo .add(i)

        for i in range(size):
            if i not in todo: # already done
                continue

            have = set()
            direction = None
            while i not in final:
                if i in have:
                    return True

                if direction is None: # all steps must have the same sign
                    direction = sign(nums[i])

                have.add(i)
                todo.discard(i)

                if sign(nums[i]) != direction: # not a cycle since direction changed
                    break

                # next step
                i += nums[i]
                i %= size

        return False
