class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # tokenize
        parts = []
        for c in formula:
            if (c.isdigit() and parts[-1].isdigit()) or ("a" <= c <= "z"):
                parts[-1] += c
            else:
                parts.append(c)

        def deeper():
            nonlocal parts
            count = defaultdict(int)

            while parts:
                token = parts.pop(0)

                if   token == "(":
                    # parse brackets
                    nested = deeper()

                    # optional factor
                    factor = 1
                    if parts and parts[0].isdigit():
                        factor = int(parts.pop(0))

                    # add all elements
                    for key, value in nested.items():
                        count[key] += factor * value
                elif token == ")":
                    break
                else:
                    # optional factor
                    factor = 1
                    if parts and parts[0].isdigit():
                        factor = int(parts.pop(0))

                    # add element
                    count[token] += factor

            return count

        # sort
        result = ""
        for name, atoms in sorted(deeper().items()):
            result += name
            if atoms > 1:
                result += str(atoms)

        return result
