class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # similiar problem as 127, but different approach

        if beginWord not in wordList:
            wordList += [ beginWord ]

        # hit => [ ".it", "h.t", "hi." ]
        def dots(w):
            for i in range(len(w)):
                yield w[:i] + "." + w[i+1:]

        offbyone = defaultdict(list)
        for w in wordList:
            for d in dots(w):
                offbyone[d].append(w)

        # pass 1: forwards
        shortest = defaultdict(set)
        shortest[0] = set([ beginWord ])
        processed   = set([ beginWord ])
        for length in range(len(wordList)):
            found = []
            for word in shortest[length]:
                for i in dots(word):
                    for next in offbyone[i]:
                        if next not in processed:
                            shortest[length + 1].add(next)
                            found.append(next)

            if endWord in found:
                break

            if not found:
                return []
            processed.update(found)

        # pass 2: backwards
        result = [ [ endWord ] ]
        step = max(shortest) - 1
        while step >= 0:
            next = []
            for ladder in result:
                first = ladder[0]
                for i in dots(first):
                    for prepend in offbyone[i]:
                        if prepend in shortest[step]:
                            next.append([ prepend ] + ladder)

            result = next
            step  -= 1

        return result
