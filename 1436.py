class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        depart = set()
        arrive = set()
        for a, b in paths:
            depart.add(a)
            arrive.add(b)

        return list(arrive - depart)[0]
