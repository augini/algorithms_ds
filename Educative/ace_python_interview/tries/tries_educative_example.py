class TrieNode:
    def __init__(self, char=""):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char


trie_node = TrieNode("e")
print(trie_node.char)


class Tree:
    def __init__(self):
        self.root = TrieNode()  # root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord("a")

    # Function to insert a key in the Trie
    # time complexity: For a word with n characters, the worst time complexity is O(n) since we make n iterations

    def insert(self, key):
        if key is None:
            return False
        key = key.lower()

        current = self.root

        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

    # Function to search a given key in Trie
    # time complexity: for a word with h letters, the worst time complexity is O(h)
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    # Function to delete given key from Trie
    def delete(self, key):
        pass
