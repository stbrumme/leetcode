class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # little bit of gambling: assume no hash collisions
        def id(s):
            return hash(s) & 0xFFFFFFF

        need = { id(r) : ( id(ii) for ii in i ) for r, i in zip(recipes, ingredients) }

        supplies = set(id(s) for s in supplies) # faster lookup
        analyzed = set()                        # known recipes plus the one currently analyzed

        @cache
        def possible(what):
            # unlimited supplies
            if what in supplies:
                return True

            # unknown recipe
            if what not in need:
                return False

            # cycle detected
            if what in analyzed:
                return False
            analyzed.add(what)

            return all(possible(n) for n in need[what])

        return [ r for r in recipes if possible(id(r)) ]
