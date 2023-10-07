class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        k = len(indices)

        # sort indices, keep relationships to sources and targets
        ordered = []
        for i, n in enumerate(indices):
            ordered.append(( n, i ))
        ordered.sort(reverse = True) # reverse order to cope with "parallel" updates
        print(ordered)

        result = s
        for pos, i in ordered:
            if pos >= len(result):
                continue

            if s[pos:].startswith(sources[i]):
                prefix = result[:pos]
                suffix = result[pos + len(sources[i]):]
                result = prefix + targets[i] + suffix

        return result
