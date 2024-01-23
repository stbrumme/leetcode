class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        # ensure that s1 always has less words than s2
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        # remove shared prefix
        while s1 and s1[0] == s2[0]:
            s1.pop(0)
            s2.pop(0)

        # remove shared suffix
        while s1 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()

        # similar if s1 is empty
        return not s1
