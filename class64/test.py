class Trie_Node:
    def __init__(self, char):
        self.val = char
        self.edges = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = Trie_Node(None)

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Trie_Node(char)
            cur_node = cur_node.edges[char]
        cur_node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(indx, diff, root):
            if indx == len(word):
                return (diff == 0) and root.isEnd

            cur_node = root
            char = word[indx]
            if char in cur_node.edges:
                cur_node = cur_node.edges[char]
                val = dfs(indx + 1, diff, cur_node)
                if val == True:
                    return True

            if diff == 1:
                diff = 0
                cur_node = root
                for c, j in cur_node.edges.items():
                    if c != char:
                        val = dfs(indx + 1, diff, j)
                        if val == True:
                            return True
            return False

        return dfs(0, 1, self.root)


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        trie = Trie()
        for i in A:
            trie.insert(i)
        ans = ''
        for j in B:
            if trie.search(j):
                ans = ans + '1'
            else:
                ans = ans + '0'
        return ans


A = ['data', 'circle', 'cricket']
B = ['date', 'circel', 'crikket', 'data', 'circl']
print(Solution().solve(A,B))