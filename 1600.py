class ThroneInheritance:
    def __init__(self, kingName: str):
        self.children = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        todo = [ self.king ]
        while todo:
            current = todo.pop()
            # next in line
            if current not in self.dead:
                result.append(current)

            # and their kids
            if current in self.children:
                todo.extend(reversed(self.children[current])) # first born last so that pop() looks at them first

        return result
