class MagicDictionary:
    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary
        
    def search(self, searchWord: str) -> bool:
        for d in self.dict:
            if len(d) == len(searchWord):
                diff = 0
                for i in range(len(d)):
                    if d[i] != searchWord[i]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    return True

        return False
