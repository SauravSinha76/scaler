from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node

        q = deque()
        q.append(node)

        clones = {node.label: UndirectedGraphNode(node.label)}

        while q:
            cur_node = q.popleft()
            cur_clone = clones[cur_node.label]

            for child in cur_node.neighbors:
                cur_child = child.label

                if cur_child not in clones:
                    clones[cur_child] = UndirectedGraphNode(cur_child)
                    q.append(child)

                cur_clone.neighbors.append(clones[cur_child])

        return clones[node.label]



node = UndirectedGraphNode(1)
node.neighbors.append(UndirectedGraphNode(2))
node.neighbors.append(UndirectedGraphNode(3))
right = UndirectedGraphNode(4)
right.neighbors.append(UndirectedGraphNode(5))
right.neighbors.append((UndirectedGraphNode(6)))
node.neighbors.append(right)
Solution().cloneGraph(node)