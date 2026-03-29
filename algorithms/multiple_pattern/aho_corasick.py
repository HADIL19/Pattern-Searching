# algorithms/multiple_pattern/aho_corasick.py

from collections import deque

class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()
        self.build_trie(patterns)
        self.build_failure_links()

    def build_trie(self, patterns):
        for pattern in patterns:
            node = self.root
            for char in pattern:
                node = node.children.setdefault(char, Node())
            node.output.append(pattern)

    def build_failure_links(self):
        queue = deque()
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)
        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                fail_node = current.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children[char] if fail_node else self.root
                child.output += child.fail.output if child.fail else []
                queue.append(child)

    def search(self, text):
        node = self.root
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            node = node.children[char] if node and char in node.children else self.root
            for pattern in node.output:
                print(f"Pattern '{pattern}' found at index {i - len(pattern) + 1}")

# Example usage
if __name__ == "__main__":
    text = "ACGTACGTGACG"
    patterns = ["ACG", "GAC"]
    ac = AhoCorasick(patterns)
    ac.search(text)