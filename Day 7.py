class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        bfs = deque([(root, None)])
        while bfs:
            n = len(bfs)
            parent = None
            foundone = False
            for _ in range(n):
                curr, par = bfs.popleft()
                if curr.val==x or curr.val==y:
                    if not foundone:
                        foundone = True
                        parent = par
                    else: return parent!=par
                if curr.right:
                    bfs.append((curr.right, curr))
                if curr.left:
                    bfs.append((curr.left, curr))
        return False
