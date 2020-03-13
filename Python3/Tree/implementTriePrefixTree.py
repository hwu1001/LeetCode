# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None]*26 # supports a-z
        self.isEnd = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def _charToIndex(self, char) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char in word:
            index = self._charToIndex(char)
            if not cur_node.children[index]:
                cur_node.children[index] = TrieNode()
            cur_node = cur_node.children[index]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self._searchForNode(word)
        return node != None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._searchForNode(prefix)
        return node != None

    def _searchForNode(self, s: str) -> TrieNode:
        cur_node = self.root
        for char in s:
            index = self._charToIndex(char)
            if not cur_node.children[index]:
                return None
            cur_node = cur_node.children[index]
        return cur_node
        
if __name__ == '__main__':
# Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert('apple')
    assert(trie.search('apple') == True)
    assert(trie.search('app') == False)
    assert(trie.startsWith('app') == True)
    trie.insert('app')
    assert(trie.search('app') == True)