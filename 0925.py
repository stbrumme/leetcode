class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        regex = ""
        for i in range(len(name)):
            regex += name[i]
            if i + 1 == len(name) or name[i] != name[i + 1]:
                regex += "+" # repeated character in name

        return re.search("^" + regex + "$", typed)
