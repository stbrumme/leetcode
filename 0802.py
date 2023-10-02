class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        loop = set()
        safe = set()
        for i, next in enumerate(graph):
            if not next:
                safe.add(i)

        def isSafe(n, seen):
            # loop detection
            if n in seen:
                for s in seen:
                    loop.add(s)
                return False

            # already processed
            if n in loop:
                return False
            if n in safe:
                return True

            # all children have to be safe
            seen.append(n)
            for next in graph[n]:
                if not isSafe(next, seen.copy()):
                    loop.add(n)
                    return False

            safe.add(n)
            return True

        # start at each node
        result = []
        for i in range(len(graph)):
            if isSafe(i, []):
                result.append(i)

        return result # == sorted(safe)
