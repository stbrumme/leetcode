class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        cars   = sorted(zip(position, speed), reverse = True)
        arrive = [ (target - p) / s for p, s in cars ] # time of arrival
        incoming = 0 # time of arrival of current fleet
        for a in arrive:
            if a <= incoming: # bump into one of the cars ahead
                fleets  -= 1
            else:
                incoming = a  # leader of a new fleet

        return fleets
