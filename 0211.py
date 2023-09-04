class WordDictionary:
    # "!" marks end of word
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for first in word:
            if first not in node:
                node[first] = {}
            node = node[first]
        node["!"] = {}

    def locate(self, node, word):
        if not word:
            return "!" in node

        first = word[0]
        if first == ".":
            for i in node:
                if self.locate(node[i], word[1:]):
                    return True
        elif first in node:
            return self.locate(node[first], word[1:])

        return False

    def search(self, word: str) -> bool:
        return self.locate(self.root, word)
