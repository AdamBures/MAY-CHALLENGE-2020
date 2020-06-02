class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        for val in self.inorder(root):
            if k == 1:
                return val
            else:
                k -= 1
        
    def inorder(self, root):
        if root is not None:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val
