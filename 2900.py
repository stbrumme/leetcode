class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        state = groups[0] ^ 1 # 1 if groups[0] == 0 else 1
        for w, g in zip(words, groups):
            if state != g:
                yield w
                state = g
