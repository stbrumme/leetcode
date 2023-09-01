class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        # hit => [ ".it", "h.t", "hi." ]
        def dots(w):
            for i in range(len(w)):
                yield w[:i] + "." + w[i+1:]

        offbyone = defaultdict(list)
        for w in wordList:
            for d in dots(w):
                offbyone[d].append(w)

        processed = set()
        steps = 1
        todo = set()
        for d in dots(beginWord):
            if d in offbyone:
                todo.update(offbyone[d])

        while todo:
            next = set()
            steps += 1

            for i in todo:
                if i == endWord:
                    return steps

                # avoid loops
                if i in processed:
                    continue
                processed.add(i)

                for d in dots(i):
                    next.update(offbyone[d])

            todo = next

        return 0
