class TextEditor:
    # heavily rely on Python's somewhat decent list implementation
    def __init__(self):
        self.data = [] # list of characters
        self.pos  = 0

    def addText(self, text: str) -> None:
        self.data[self.pos : self.pos] = [ c for c in text ]
        self.pos += len(text)

    def deleteText(self, k: int) -> int:
        k = min(k, self.pos) # careful if not enough characters
        self.data[self.pos - k : self.pos] = []
        self.pos -= k
        return k

    def cursorLeft(self, k: int) -> str:
        self.pos -= min(self.pos, k) # careful if not enough characters
        return "".join(self.data[max(self.pos - 10, 0) : self.pos])

    def cursorRight(self, k: int) -> str:
        self.pos = min(len(self.data), self.pos + k)
        return "".join(self.data[max(self.pos - 10, 0) : self.pos])
