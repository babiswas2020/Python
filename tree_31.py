class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def postorder(node):
    stack=[]
    root=node
    while True:
        if root:
            stack.append(root)
            root=root.left
        else:
            if not stack:
                break
            else:
                if stack[-1].right==None:
                    root=stack.pop()
                    print(root.value)
                    while root==stack[-1].right:
                        root=stack.pop()
                        print(root.value)
                        if not stack:
                            break
                if stack:
                    root=stack[-1].right
                else:
                    root=None

if __name__=="__main__":
    node=Node(12)
    node.left=Node(6)
    node.right=Node(21)
    node.right.left=Node(18)
    node.right.right=Node(24)
    node.left.right=Node(4)
    node.left.left=Node(7)
    node.left.left.right=Node(9)
    node.left.left.left=Node(17)
    print("Printing post order traversal")
    postorder(node)

              