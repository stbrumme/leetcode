class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        inside = False # true if inside a C-style comment /* */
        code   = ""    # code without comments, may span several input lines

        for s in source:
            skip = False # skip next character
            for i in range(len(s)):
                if skip:
                    skip = False
                    continue

                one = s[i]         # current character
                two = s[i : i + 2] # current and the next character

                if inside:
                    if two == "*/": # end of C-style comment
                        inside = False
                        skip   = True
                else:
                    if two == "//": # C++ comment: ignore rest of the line
                        break
                    if two == "/*": # start C-style comment
                        skip   = True
                        inside = True
                    else:           # no comment ...
                        code += one

            if code and not inside: # skip empty lines
                yield code
                code = ""
