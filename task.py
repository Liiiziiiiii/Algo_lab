class TrieNode:
    def __init__(self):
        self.end = False
        self.words = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.words:
                node = node.words[char]
            else:
                new_node = TrieNode()
                node.words[char] = new_node
                node = new_node
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.words:
                node = node.words[char]
            else:
                return False
        return node.end

    def prefix(self, word):
        node = self.root

        for char in word:
            if char in node.words:
                node = node.words[char]
            else:
                return False

        return True

def main():
    t = Trie()
    t.insert("something")
    t.insert("many")
    t.insert("none")
    t.insert("what")
    t.insert("where")

    result = t.prefix("wh")
    print("wh - ", result)
    result_pr = t.prefix("op")
    print("op - ", result_pr)
    result2 = t.search("some")
    print("some - ", result2)
    s = t.search("something")
    print("something - ", s)


if __name__ == '__main__':
    main()
