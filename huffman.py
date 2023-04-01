from typing import List, Dict, Tuple


class Node:
    """
    Describes a Node inside the NodeQueue.
    Nodes that have len(self.string) == 1 are leaves, otherwise they are 
    internal nodes.
    """
    def __init__(self, string: str, count: int, right=None, left=None) -> None:
        self.string = string
        self.count = count # How frequently the character occurs in the plaintext.
        self.right = right
        self.left = left
    
    def __str__(self) -> str:
        return f'(string: {self.string}, count: {self.count})'
    
    def __eq__(self,  other) -> bool:
        return self.__dict__ == other.__dict__


class NodeQueue: # Priority queue for nodes. Lower count -> higher priority.
    def __init__(self, char_counts: Dict[str, int]) -> None:
        self.l: List[Node] = []
        for string, count in char_counts.items():
            self.push(Node(string, count))
    
    def push(self, node: Node) -> None:
        self.l.append(node)
    
    # Remove and return minimum node based on count.
    def pop(self) -> Node:
        val_min = self.l[0].count
        i_min = 0
        # Linear search to find minimum.
        for i in range(1, len(self.l)):
            if self.l[i].count < val_min:
                val_min = self.l[i].count
                i_min = i
        return self.l.pop(i_min)
    
    def pop2(self) -> Tuple[Node, Node]:
        return self.pop(), self.pop()
    
    def length(self) -> int:
        return len(self.l)


# Count how many times each character occurs.
def get_char_counts(plaintext: str) -> Dict[str, int]:
    d = {}
    for ch in plaintext:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    return d


# Leafs are single character nodes.
def codes_from_tree(root: Node) -> Dict[str, str]:
    codes = {}
    def f(node: Node | None, code: str):
        if node:
            if len(node.string) == 1:
                codes[node.string] = code
            f(node.right, code + '0')
            f(node.left, code + '1')
    f(root, '')
    return codes


# Output the codes for each character.
def get_huff_codes(plaintext: str) -> Dict[str, str]:
    char_counts = get_char_counts(plaintext)
    node_queue = NodeQueue(char_counts)
    while node_queue.length() > 1:
        a, b = node_queue.pop2()
        c = Node(a.string + b.string, a.count + b.count, a, b)
        node_queue.push(c)
    root = node_queue.pop()
    return codes_from_tree(root)
