class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        have = set()
        for f in sorted(folder):
            sub   = False       # subfolder
            parts = f.split("/")
            build = ""
            for p in parts[1:]: # skip the initial string, it's always empty
                build += "/" + p
                if build in have:
                    sub = True
                    break
            have.add(f)

            if not sub:
                yield f
