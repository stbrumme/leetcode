class SORTracker:
    def __init__(self):
        self.data = []
        self.queries = 0

    def add(self, name: str, score: int) -> None:
        insort(self.data, ( -score, name )) # trick: negative numbers to sort in descending order
                                            #        => highest score first

    def get(self) -> str:
        score, name = self.data[self.queries]
        self.queries += 1
        return name
