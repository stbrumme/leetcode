class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # an apple a day keeps Leetcode problems away ...
        if not any(hasApple):
            return 0

        # collect edges
        branches = defaultdict(list)
        for a, b in edges:
            branches[a].append(b)
            branches[b].append(a)

        seen = [ False ] * n

        # count travelled edges including the incoming one (only if there is at least one apple)
        def deeper(pos):
            nonlocal seen
            seen[pos] = True

            # walk to our branch and back
            step = 2

            seconds = 0
            for other in branches[pos]:
                # ignore if already processed
                if seen[other]:
                    continue

                more = deeper(other)
                if more > 0:
                    # walk this path to apples on sub-branches
                    # doesn't matter if there is an apple on the current branch
                    seconds += more

            # add incoming edge (only if apples found in subtree, skip at root)
            if pos != 0 and (seconds > 0 or hasApple[pos]):
                seconds += 1 + 1

            return seconds

        return deeper(0)
