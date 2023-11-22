class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # too short
        if len(s) < k:
            return 0

        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        skip = []
        for p in pos:
            if len(pos[p]) < k:
                skip += pos[p]

        # all letters appear  often enough
        if not skip:
            return len(s)
        # no  letter  appears often enough
        if len(skip) == len(s):
            return 0

        # subdivide
        result = 0
        left = 0
        for right in sorted(skip) + [ ]:
            result = max(result, self.longestSubstring(s[left : right], k))
            left = right + 1
        # final segment
        result = max(result, self.longestSubstring(s[left:], k))

        return result
