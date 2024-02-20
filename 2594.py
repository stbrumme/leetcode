class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # speed trick: in many test cases, multiple mechanics have the same rank
        mechanics = defaultdict(int)
        for r in ranks:
            mechanics[r] += 1

        def finishCars(minutes):
            # cars that can be finished within x minutes
            result = 0
            for rank, count in mechanics.items():
                slots   = minutes // rank
                cars    = int(sqrt(slots))
                result += cars * count
            return result

        # fastest mechanic has lowest rank
        fast       = min(mechanics)
        # fastest person repairs at least one car and at most all cars
        candidates = range(fast * cars * cars + 1)

        return bisect_left(candidates, cars, key = lambda x: finishCars(x))
