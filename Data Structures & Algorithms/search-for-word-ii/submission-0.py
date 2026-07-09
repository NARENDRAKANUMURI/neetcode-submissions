class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for word in words:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
            node.endOfWord=True
        rows,cols,result=len(board),len(board[0]),[]
        def dfs(r,c,node,word):
            ch=board[r][c]

            if ch not in node.children:
                return 
            node=node.children[ch]
            word+=ch

            if node.endOfWord:
                result.append(word)
                node.endOfWord=False
                
            board[r][c]="#"

            if r>0 and board[r-1][c]!="#":
                dfs(r-1,c,node,word)

            if r<rows-1 and board[r+1][c]!="#":
                dfs(r+1,c,node,word)

            if c>0 and board[r][c-1]!="#":
                dfs(r,c-1,node,word)
            
            if c<cols-1 and board[r][c+1]!="#":
                dfs(r,c+1,node,word)

            board[r][c]=ch

            if not node.children and not node.endOfWord:
                del node
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return result
            