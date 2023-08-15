class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        result = []
        for word in sentence.split():
            found = False
            current = ""
            for c in word:
                current += c
                if current in roots:
                    result.append(current)
                    found = True
                    break

            if not found:
                result.append(word)

        return " ".join(result)
