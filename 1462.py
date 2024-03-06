class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        all = [ [ False ] * numCourses for _ in range(numCourses) ]
        for a, b in prerequisites:
            all[a][b] = True

        for mid in range(numCourses):
            for a in range(numCourses):
                if all[a][mid]:
                    for b in range(numCourses):
                        all[a][b] |= all[mid][b]

        for a, b in queries:
            yield all[a][b]
