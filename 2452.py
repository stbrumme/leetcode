class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # remove duplicates
        dictionary = set(dictionary)

        # brute force
        for q in queries:
            for d in dictionary:
                diff = 0
                # compare letters, stop if more than 2 differences
                for a, b in zip(q, d):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break

                # match, don't look any further in the dictionary
                if diff <= 2:
                    yield q
                    break
