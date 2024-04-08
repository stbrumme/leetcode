class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        prefix = defaultdict(int)

        for n in names:
            # new name (maybe it's the old if not used yet)
            filename = n

            # increment counter until there is no collision
            while filename in prefix:
                filename = n + "(" + str(prefix[n]) + ")"
                prefix[n] += 1

            # block that filename from further usage
            prefix[filename] = 1
            yield filename
