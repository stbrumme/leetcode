class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        dx = uniform(-self.r, +self.r)
        dy = uniform(-self.r, +self.r)
        while dx*dx + dy*dy > self.r*self.r:
            dx = uniform(-self.r, +self.r)
            dy = uniform(-self.r, +self.r)
        return [ self.x + dx, self.y + dy ]
