class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # simply brute force with a little caching

        # positions of each letter
        letters = defaultdict(list)
        for i, c in enumerate(ring):
            letters[c].append(i)

        @cache
        def deeper(index = 0, rotation = 0): # index => position in key
            if index == len(key):
                return 0

            best = 9999
            for i in letters[key[index]]:
                # consider wraparound, too
                closest = min(abs(rotation - i), len(ring) - abs(rotation - i))
                steps = closest + deeper(index + 1, i)
                best  = min(best, steps)

            return best + 1 # press button, too

        return deeper()
