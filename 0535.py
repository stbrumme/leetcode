class Codec:
    urls = {}

    def encode(self, longUrl: str) -> str:
        shortUrl = "https://tinyurl.com/" + str(abs(hash(longUrl)))
        print(shortUrl)
        self.urls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]
