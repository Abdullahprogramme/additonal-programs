class Node():
    def __init__(self):
        self.word = {}
        self.end = False
    
class Trie():
    def __init__(self):
        self.start = Node()

    def Insert(self, word):
        cur = self.start
        for letter in  word:
            if letter not in cur.word:
                cur.word[letter] = Node()
            cur = cur.word[letter]
        cur.end = True

    def Search(self, word):
        cur = self.start
        for letter in word:
            if letter not in cur.word:
                return False
            cur = cur.word[letter]
        return cur.end

me = Trie()
me.Insert("Abdullah")
me.Insert("Tariq")
print(me.Search("Abdullah"))