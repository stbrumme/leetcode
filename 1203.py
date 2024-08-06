class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        size = n # == len(beforeItems)

        # topological sort
        def topsort(item, need, visited, output):
            # recursive implementation

            # each item only once
            if item in visited:
                return
            visited.add(item)

            # visit prerequisites
            for next in need[item]:
                topsort(next, need, visited, output)

            # found the proper position
            output.append(item)

        # wrapper for topsort
        def mysort(need):
            output  = []
            visited = set()

            if isinstance(need, list):
                keys = range(len(need)) # list
            else:
                keys = need.keys()      # dict

            for node in keys:
                topsort(node, need, visited, output)

            # consistency check (loops are not allowed)
            have = set()
            for o in output:
                for n in need[o]:
                    if n not in have:
                        return [] # cyclic dependency found
                have.add(o)

            return output

        # convert "no group" to unique group ids
        limit = max(group) + 1
        for item in range(size):
            if group[item] == -1:
                group[item] = limit
                limit      += 1

        # slice items into groups (I call them "blocks")
        blocks = [ [] for _ in range(limit) ]
        for item in range(size):
            blocks[group[item]].append(item)

        # order of blocks
        order = [ [] for _ in range(limit) ] # I tried defaultdict(set) first,
                                             # but lists are even faster for the given input
                                             # despite their O(n) lookup

        # sort each block
        for id in range(limit):
            if not blocks[id]:
                continue # unused group ID

            # extract prerequisites that happen to be in the same block
            need = { s: [] for s in blocks[id] }
            for s in blocks[id]:
                for b in beforeItems[s]:
                    if b in blocks[id]:
                        # depends on an item in the same block
                        need [s] .append(b)
                    else:
                        # depends on an item in a different block
                        order[id].append(group[b])

            blocks[id] = mysort(need)
            # abort if cycle was found
            if not blocks[id]:
                return []

        # sort blocks
        output = mysort(order)

        # push, push, push !
        for o in output:
            if blocks[o]:
                yield from blocks[o]
