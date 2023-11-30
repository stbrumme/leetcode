class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        id    = 0  # unique ID during traversal
        leafs = [] # check only leaf nodes

        # add node.parent to each child and a unique ID
        def findParent(node, parent):
            if node:
                nonlocal id
                # inject parent
                node.parent = parent
                node.id     = id
                id         += 1

                if node.left or node.right:
                    # going deeper
                    findParent(node.left,  node)
                    findParent(node.right, node)
                else:
                    # store leaf node
                    leafs.append(node)

        # identify all leaf nodes and track their parent
        findParent(root, None)

        # find common parent of two nodes (helper for count())
        def ancestor(left, right):
            visited = set()

            scan = left
            while scan:
                visited.add(scan.id)
                scan = scan.parent

            scan = right
            while scan:
                if scan.id in visited:
                    # found shared parent
                    return scan

                scan = scan.parent

        # length(left, parent) + length(right, parent)
        def count(left, right):
            edges  = 0
            parent = ancestor(left, right)

            scan = left
            while scan != parent:
                scan   = scan.parent
                edges += 1

            scan = right
            while scan != parent:
                scan   = scan.parent
                edges += 1

            return edges

        result = 0
        for i in range(len(leafs)):
            for j in range(i + 1, len(leafs)):
                if count(leafs[i], leafs[j]) <= distance:
                    result += 1
        return result
