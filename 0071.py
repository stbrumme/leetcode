class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")

        again = True
        while again:
            again = False
            for i in range(len(parts)):
                if parts[i] == "" or parts[i] == ".":
                    del parts[i]
                    again = True
                    break

                if parts[i] == "..":
                    del parts[i]
                    if i > 0:
                        del parts[i-1]
                    again = True
                    break

        return "/" + "/".join(parts)
