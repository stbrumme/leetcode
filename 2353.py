class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.scores = defaultdict(int)
        self.styles = defaultdict(str)
        self.best   = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.scores[f] = r
            self.styles[f] = c

            self.best  [c].append(( -r, f )) # max-heap => negative score

        for c in self.best:
            heapify(self.best[c])

    def changeRating(self, food: str, newRating: int) -> None:
        self.scores[food] = newRating

        # add to heap (creates duplicates, resolved in highestRated())
        c = self.styles[food]
        heappush(self.best[c], ( -newRating, food ))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.best[cuisine][0]

            # compare against current score, maybe we have stale data
            if self.scores[food] == -rating: # remember: max-heap, therefore negative score
                return food

            # remove garbage and try again
            heappop(self.best[cuisine])
