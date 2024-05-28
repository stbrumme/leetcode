class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # extract letters
        letters = []
        for l in logs:
            if l[-1] > "9":
                id, content = l.split(" ", 1)
                letters.append(( content, id ))

        # sort them
        for content, id in sorted(letters):
            yield id + " " + content

        # unsorted digits
        for l in logs:
            if l[-1] <= "9":
                yield l
