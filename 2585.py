class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        @cache
        def deeper(points, category):
            # no more questions
            if category == len(types):
                return 1 if points == target else 0

            # reached target
            if points == target:
                return 1

            # keep asking
            result = 0
            count, marks = types[category]
            for i in range(count + 1):
                result += deeper(points, category + 1)
                points += marks
                if points > target:
                    break

            return result % 1_000_000_007

        return deeper(0, 0)
