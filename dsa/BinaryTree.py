from collections import deque
from TreeNode import TreeNode


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
    
def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False
    
def levelOrder(root):
    res = []
    if root is None:
        return res
    res.append([root.val])
    q = deque()
    q.append(root)
    while(q):
        child = []
        curr = q.popleft()
        print(curr.val)
        if curr.left:
            q.append(curr.left)
            child.append(curr.left.val)
        if curr.right:
            q.append(curr.right)
            child.append(curr.right.val)
        if len(child) > 0:
            res.append(child)
    print(res)
  
def iterativeInorder(root):
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right
    

def kthSmallest(root,k):
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            print(curr.val)
        curr = curr.right

'''
    3
   / \
  1   4
   \  
    2
'''  

def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.right = TreeNode(3)
    kthSmallest(root,1)
    

    
    

if __name__ == '__main__':
    main()
    
        