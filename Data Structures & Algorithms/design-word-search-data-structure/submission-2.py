class DictNode:
    def __init__(self):
        self.children={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = DictNode()
            curr=curr.children[ch]
        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.isEnd
        return dfs(0,self.root)
                    

        
        




