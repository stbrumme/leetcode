class Solution:
    def countCollisions(self, directions: str) -> int:
        # strip cars going "out of bounds"
        mid = directions.lstrip("L").rstrip("R")

        # three cases:
        # cars R and S crash: 1 point
        # cars S and L crash: 1 point
        # cars R and L crash: 2 points
        # counting "R" and "L" is enough
        return mid.count("R") + mid.count("L")
