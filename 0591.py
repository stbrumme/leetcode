class Solution:
    def isValid(self, code: str) -> bool:
        # code must be wrapped in a tag
        if len(code) < 2:
            return False
        if code[0] != "<" or code[-1] != ">":
            return False

        size    = len(code)
        comment = False
        close   = [] # stack
        skip    = 0  # ignore these characters

        for i in range(size):
            next = code[i :]

            # skip because its still a closing tag
            if skip > 0:
                skip -= 1
                continue

            if not close and i > 0:
                return False # outermost tag closed too early

            # comment
            if comment:
                if next.startswith("]]>"):
                    comment = False
                    skip    = len(close.pop()) - 1
                continue

            if next.startswith("<![CDATA["):
                comment = True
                close.append("]]>")
                skip = 8 # len("<![CDATA[") - 1
                continue

            # close a tag
            if close and next.startswith(close[-1]):
                skip = len(close.pop()) - 1
                continue

            if next[0] != "<":
                continue

            # open a new tag
            stop = next.find(">")
            # each "<" needs a ">" (which isn't clear from the description)
            if stop == -1:
                return False
            # create its closing tag
            tag = next[1 : stop]
            # uppercase only, 1..9 characters
            if not tag.isupper() or not tag.isalpha() or not (1 <= len(tag) <= 9):
                return False

            skip = stop
            close.append("</" + tag + ">")

        # stack must be empty => all tags closed
        return not close
