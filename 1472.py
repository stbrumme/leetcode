class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [ homepage ]
        self.pos     = 0

    def visit(self, url: str) -> None:
        if self.pos < len(self.history) - 1:
            self.history = self.history[:self.pos + 1]
        self.history.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos -= steps
        self.pos  = max(self.pos, 0)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos += steps
        self.pos  = min(self.pos, len(self.history) - 1)
        return self.history[self.pos]
