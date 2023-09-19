class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # reverse order, first by height then position
        people.sort(key = lambda x : -x[0]*10**7 + x[1])

        result = []
        for p in people:
            result.insert(p[1], p)
        return result
