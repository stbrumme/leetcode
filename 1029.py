class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        # process highest price deltas first
        costs.sort(reverse = True, key = lambda x: abs(x[0] - x[1]))

        # number of persons flying to a or b
        one = two = 0

        result = 0
        for a, b in costs:
            # prefer the cheaper flight unless destination city is already fully booked
            if (a < b and one < n) or two == n:
                result += a
                one    += 1
            else:
                result += b
                two    += 1

        return result
