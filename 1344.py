class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes / 60
        h = hour / 12 + m / 12

        angle = h - m
        if angle < 0:
            angle += 1
        if angle > 0.5:
            angle  = 1 - angle

        return 360 * angle
