class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()

            curr = curr.children[char]
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.isEnd
            
            char = word[i]

            if char != ".":
                if char not in curr.children:
                    return False
                
                return dfs(i+1, curr.children[char])

            for child in curr.children.values():
                if dfs(i+1, child):
                    return True
            return False
        return dfs(0, self)




        
