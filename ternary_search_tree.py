class TernarySearchTree:
    #Tree initialization 
    def __init__(self):
        self.root = None #Because there are no words yet
        self.word_count = 0 #Keeps track of how many words are inserted
        self.words_list = [] #Keeps track of all inserted words

    #Node initialization
    class Node:
        def __init__(self, char):
            self.char = char #Character that is stored in the node
            self.end_of_word = False #False when the letter is the end of the word, True otherwise
            self._ls = None #Next node that has a character lesser
            self._eq = None #Next node that is the following character of the word
            self._gt = None #Nets node that has a character greater
            
    def insert(self, word):
        self.words_list.append(word) #updates list of all words
        self.word_count += 1 #updates the number of words added

    def __len__(self):
        return self.word_count #returns number of words

    def all_strings(self):
        return self.words_list #returns list of words
