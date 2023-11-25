class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # maybe I could traverse only "cloned" and ignore "original"
        if not original:
            return None

        if original.val == target.val: # same as cloned.val == target.val
            return cloned

        return self.getTargetCopy(original.left,  cloned.left,  target) or \
               self.getTargetCopy(original.right, cloned.right, target)
