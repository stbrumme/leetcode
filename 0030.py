class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        shift = len(words[0])
        size  = len(words) * shift

        result = []

        for offset in range(shift):
            need = defaultdict(int)
            for w in words:
                need[w] += 1

            # initial block
            pos = offset
            for _ in range(len(words)):
                next = s[pos : pos + shift]
                need[next] -= 1
                if need[next] == 0:
                    del need[next]
                pos += shift

            if len(need) == 0:
                result.append(offset)

            # sliding window
            for left in range(offset, len(s) - size, shift):
                right = left + size
                remove = s[left  : left  + shift]
                add    = s[right : right + shift]

                need[remove] += 1
                need[add]    -= 1

                if need[remove] == 0:
                    del need[remove]
                if need[add]    == 0:
                    del need[add]
                if len(need) == 0:
                    result.append(left + shift)

        return result
