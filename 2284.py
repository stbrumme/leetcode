class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        words = defaultdict(int)
        for m, s in zip(messages, senders):
            words[s] += len(m.split(" "))

        high = max(words.values())
        for w in sorted(words.keys(), reverse = True):
            if words[w] == high:
                return w
