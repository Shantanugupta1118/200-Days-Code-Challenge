# Github: Shantanugupta1118
# Day 133 of day 200
# 133. Clone Graph - Leetcode


from logging.config import valid_ident


class Node:
    def __init__(self, val=0, neighbours=None) -> None:
        self.val = val
        self.neighbours = None



class Solution:
    def cloneGraph(self, node):
        def dfs(node, hashmap):
            if not node: return None
            if node.val in hashmap:
                return hashmap[node.val]
            clone = Node(node.val)
            hashmap[node.val] = clone
            for n in node.neighbours:
                clone.neighbors.append(dfs(n, hashmap))
            return clone

        return dfs(node, {})




