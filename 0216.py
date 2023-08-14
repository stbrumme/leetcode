class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        current = [ [ ] ]
        for i in range(9, 0, -1):
            next = []
            for j in current:
                if len(j) == k - 1:
                    if i + sum(j) == n:
                        result.append(j + [i])
                elif i + sum(j) <= n:
                    next.append(j + [i])

            current = current + next

        return result
