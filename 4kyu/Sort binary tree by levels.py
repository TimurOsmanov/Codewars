class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


answer, answer2, i = [], [], 0


def tree_by_levels1(node):
    global answer, i, answer2
    if node:
        if i == 0:
            node = [node.value, node.left, node.right]
            i += 1
        temp, answer = [], []
        for x in node:
            if isinstance(x, int):
                temp.append(x)
            else:
                if x:
                    temp.append(x.value)
                    if x.left is not None:
                        answer.append(x.left)
                    if x.right is not None:
                        answer.append(x.right)
        answer2.append(temp)
        tree_by_levels1(answer)
        return [y for x in answer2 for y in x]
    else:
        return []


def tree_by_levels(node):
    global answer, answer2, i
    ans = tree_by_levels1(node)
    answer, answer2, i = [], [], 0
    return ans

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
# best practice
# def tree_by_levels(node):
#     nodes = [node] if node else []
#     for node in nodes:
#             if node.left:
#                 nodes.append(node.left)
#             if node.right:
#                 nodes.append(node.right)
#     return list(node.value for node in nodes)

