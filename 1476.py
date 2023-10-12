class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.original = rectangle
        self.updates = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append(( row1, col1, row2, col2, newValue ))

    def getValue(self, row: int, col: int) -> int:
        # scan updates in reverse order
        for i in range(len(self.updates) - 1, -1, -1):
            row1, col1, row2, col2, value = self.updates[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value

        # fallback to the original grid
        return self.original[row][col]
