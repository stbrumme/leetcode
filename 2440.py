class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        size  = len(nums)
        total = sum(nums)

        next = [ list() for _ in range(size) ]
        for a, b in edges:
            next[a].append(b)
            next[b].append(a)

        def deeper(node, previous):
            have = nums[node]
            for n in next[node]:
                if n != previous:
                    have += deeper(n, node)
                    if have > limit:
                        break

            if have == limit:
                have = 0 # delete edge

            return have

        for cuts in reversed(range(1, size)):
            limit, remaining = divmod(total, cuts + 1)
            if remaining == 0 and deeper(0, -1) == 0: # start at any node, pick 0
                return cuts

        return 0
