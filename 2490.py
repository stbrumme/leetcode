class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        return all(a[-1] == b[0] for a, b in zip(words, words[1:])) and words[0][0] == words[-1][-1]
