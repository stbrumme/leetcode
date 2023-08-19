class Solution:

    def createEdges(self, node):
        if not node or node.val in self.edges:
            return

        self.edges[node.val] = []
        for i in node.neighbors:
            self.edges[node.val].append(i.val)
            self.createEdges(i)


    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        self.edges = {}
        self.createEdges(node)

        clone = {}
        for e in self.edges:
            clone[e] = Node(e)

        for e in self.edges:
            for other in self.edges[e]:
                clone[e].neighbors.append(clone[other])

        return clone[node.val]
