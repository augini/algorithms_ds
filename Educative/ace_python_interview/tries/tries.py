from collections import deque


class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None:
            return None
        curr = self.root

        for char in word:
            # if not exist, create a node
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            # if exists, move to that node
            curr = curr.children[char]

        curr.endOfWord = True

        return None

    def search(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # if exists, check it is denoted as end of word
        return curr.endOfWord

    def startsWith(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    def countWords(self):
        if not self.root:
            return 0

        q = deque([self.root])
        wordsCount = 0
        while q:
            curr = q.popleft()

            if curr.children:
                for value in curr.children.values():
                    if value.endOfWord == True:
                        wordsCount += 1
                    q.append(value)
        return wordsCount

    def delete(self, s) -> bool:
        # create a recursive helper function that takes 3 arguments: curr node, string and curr index and returns a boolean
        def rec_delete(node: TrieNode, s: str, i: int) -> bool:
            # base case: check curr index is equal to the lenght of the string, indicating we are at the last node
            if i == len(s):
                # set endOfWord of last node to False, return a boolean denoting if the last node has any children
                node.endOfWord = False
                return len(node.children) == 0
            else:
                keepDeleting = rec_delete(node.children[s[i]], s, i + 1)
                # continue deleting nodes if endOfWord for that node is False, doesn't have any children
                if keepDeleting:
                    del node.children[s[i]]
                return keepDeleting and node.endOfWord and len(node.children) == 0

        rec_delete(self.root, s, 0)
        return True

    def retrieveAllWords(self) -> list[str]:
        s = [(self.root, "")]
        all = []
        while len(s):
            curr, string = s.pop()

            if curr.endOfWord:
                all.append(string + curr.char)

            if curr.children:
                for child in curr.children.values():
                    s.append((child, string + curr.char))

        return sorted(all)


Words = Trie()

Words.insert("apple")
Words.insert("carpet")
Words.insert("car")
Words.insert("hello")

# print(Words.retrieveAllWords())


dictionary = ["the", "hello", "there", "answer", "any", "by", "world", "their", "abc"]
word = "helloworld"


def is_formation_possible(dictionary, word):
    # Write your code here
    words = Trie()

    for w in dictionary:
        words.insert(w)

    # start with the first char
    curr = words.root
    for i in range(len(word)):
        if curr.endOfWord:
            if words.search(word[i:]):
                return True
            else:
                continue

        char = word[i]
        if char in curr.children:
            curr = curr.children[char]
    return False


print(is_formation_possible(dictionary, word))
