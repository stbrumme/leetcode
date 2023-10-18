class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl    = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        deadline = currentTime + self.ttl
        self.tokens[tokenId] = deadline

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            deadline = currentTime + self.ttl
            if  self.tokens[tokenId] > currentTime:
                self.tokens[tokenId] = deadline # similar to generate()

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for t in self.tokens if self.tokens[t] > currentTime)
