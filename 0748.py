class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # sort letters, then regex matching
        abc = re.sub("[^a-z]", "", licensePlate.lower()) # remove garbage
        abc = re.compile(".*".join(sorted(list(abc))))

        result = ""
        for w in words:
            s = "".join(sorted(list(w)))
            if abc.search(s):
                if result == "" or len(result) > len(w):
                    result = w

        return result
