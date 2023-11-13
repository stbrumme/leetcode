class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        likes = defaultdict(set)
        for i, favs in enumerate(favoriteCompanies):
            for f in favs:
                likes[f].add(i)

        for i, favs in enumerate(favoriteCompanies):
            same  = set()
            first = True
            for f in favs:
                if first:
                    same  = likes[f].copy()
                    first = False
                else:
                    same &= likes[f]

            if len(same) == 1:
                yield i
