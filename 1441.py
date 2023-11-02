class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        for i in range(1, n + 1):
            yield "Push"
            if i == target[0]:
                del target[0]
                if not target:
                    break
            else:
                yield "Pop"
