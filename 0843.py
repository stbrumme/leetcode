class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        while True:
            # try a random word
            candidate = random.choice(words)
            matches   = master.guess(candidate)
            if matches == 6:
                return

            # only those remain in wordlist that have the same number of matches
            next = []
            for w in words:
                same = sum([ a == b for a, b in zip(candidate, w) ])
                if same == matches:
                    next.append(w)
            words = next
