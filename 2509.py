class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for a, b in queries:
            # find distance to common ancestor of a and b
            steps = 1 # plus the new edge
            while a != b:
                while a > b:
                    a    >>= 1
                    steps += 1
                while b > a:
                    b    >>= 1
                    steps += 1

            yield steps
