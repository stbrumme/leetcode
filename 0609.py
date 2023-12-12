class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for p in paths:
            directory = p.split(" ")
            path = directory.pop(0)          # first item is the path
            for file in directory:           # followed by files
                name, text = file.split("(") # keep final ")", it doesn't matter
                content[text].append(path + "/" + name)

        for c in content:
            if len(content[c]) > 1:
                yield content[c]
