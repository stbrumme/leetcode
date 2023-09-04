class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        needmore = defaultdict(set)
        for p in prerequisites:
            needmore[p[0]].add(p[1])

        resolved = set(range(numCourses)) - needmore.keys()

        again = True
        while again:
            again = False

            remove = set()
            for n in needmore:
                reduce = needmore[n].intersection(resolved)
                if reduce:
                    again = True
                    if len(reduce) == len(needmore[n]):
                        resolved.add(n)
                        remove.add(n)
                    else:
                        needmore[n] -= reduce

            for r in remove:
                del needmore[r]

        return len(needmore) == 0
