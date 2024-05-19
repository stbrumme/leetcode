class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # store top element of each triangle
        up = defaultdict(str)
        for a in allowed:
            up[a[ : 2]] += a[2]

        @cache
        def deeper(row, next = ""):
            if len(row) == 1:
                # final triangle
                if not next:
                    return True
                # begin new row
                return deeper(next, "")

            return any(deeper(row[1 :], next + u) for u in up[row[: 2]])

        return deeper(bottom)
