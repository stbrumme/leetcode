class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        a = ""
        for word in sentence.split(" "):
            a += "a"
            if word[0].lower() in [ "a", "e", "i", "o", "u" ]:
                result.append(word + "ma" + a)
            else:
                result.append(word[1:] + word[0] + "ma" + a)

        return " ".join(result)
