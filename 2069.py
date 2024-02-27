class Robot:
    def __init__(self, width: int, height: int):
        # precompute the full path (it's always along the walls/borders)
        self.path = []
        for x in range(1, width):
            self.path.append((x,          0, "East"))
        for y in range(1, height):
            self.path.append((width - 1,  y, "North"))
        for x in reversed(range(width - 1)):
            self.path.append((x, height - 1, "West"))
        for y in reversed(range(height - 1)):
            self.path.append((0,          y, "South"))

        # initially at (0, 0) which is the last position of the full path
        self.pos     = -1
        self.started = False # the robot is facing south if standing on (0, 0)
                             # except for the start, when it is facing east

    def step(self, num: int) -> None:
        self.started = True

        self.pos += num
        # wrap-up
        self.pos %= len(self.path)

    def getPos(self) -> List[int]:
        return self.path[self.pos][:2] # (x, y)

    def getDir(self) -> str:
        return self.path[self.pos][2] if self.started else "East"
