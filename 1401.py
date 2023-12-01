class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # check bounding box
        if x1 > xCenter + radius or y1 > yCenter + radius:
            return False
        if x2 < xCenter - radius or y2 < yCenter - radius:
            return False

        # check if x,y is inside the rectangle
        insideRect   = lambda x, y: x1 <= x <= x2 and y1 <= y <= y2
        # check if x,y is inside the circle
        insideCircle = lambda x, y: sqrt((x - xCenter)**2 + (y - yCenter)**2) <= radius

        # top/right/bottom/left of the circle
        if insideRect(xCenter + radius, yCenter) or insideRect(xCenter - radius, yCenter):
            return True
        if insideRect(xCenter, yCenter + radius) or insideRect(xCenter, yCenter - radius):
            return True

        # corners of the rectangle
        if insideCircle(x1, y1) or insideCircle(x1, y2) or \
           insideCircle(x2, y1) or insideCircle(x2, y2):
            return True


        # randomized approach

        # sample a few points
        samples = 1000
        for _ in range(samples):
            angle = randint(0, 360) / 180 * pi
            # on the circumference
            x = xCenter + cos(angle) * radius
            y = yCenter + sin(angle) * radius
            if insideRect(x, y):
                return True

            # and inside the circle
            distance = randint(0, radius)
            x = xCenter + cos(angle) * distance
            y = yCenter + sin(angle) * distance
            if insideRect(x, y):
                return True

            # random integer coordinates inside the circle
            x = xCenter + randint(-radius, +radius)
            y = yCenter + randint(-radius, +radius)
            d = sqrt(x*x + y*y)
            if d <= radius and insideRect(x, y):
                return True

            # random integer coordinates inside the rectangle
            x = randint(x1, x2)
            y = randint(y1, y2)
            if insideCircle(x, y):
                return True
            # and on its border
            if insideCircle(x1, y) or insideCircle(x2, y) or \
               insideCircle(x, y1) or insideCircle(x, y2):
               return True

        return False
