class TernarySearchTree:
    #Tree initialization 
    def __init__(self):
        self.root = None #Because there are no words yet
        self.word_count = 0 #Keeps track of how many words are inserted
        self.words_list = [] #Keeps track of all inserted words

    #Node initialization
    class Node:
        def __init__(self, char):
            self.char = char #Letter that is stored in the node
            self.end_of_word = False #True when the letter is the end of the word
            self._ls = None #Next node that has a character lesser
            self._eq = None #Next node that is the following character of the word
            self._gt = None #Nets node that has a character greater

    #Length of the tree
    def __len__(self):
        return self.word_count #returns number of words

    #Words inside the tree
    def all_strings(self):
        return self.words_list #returns list of words

    #Helper function for inserting words
    def insert_character(self, node, word, index):
        char = word[index] #character to insert

        if node is None:
            node = self.Node(char) #creates a new node if there is none already

        if char < node.char:
            node._ls = self.insert_character(node._ls, word, index) #go left
        elif char > node.char:
            node._gt = self.insert_character(node._gt, word, index) #go right
        else:
            if index + 1 == len(word):
                node.end_of_word = True #marks as end of the word
            else:
                node._eq = self.insert_character(node._eq, word, index + 1) #go middle

        return node

    #Insert word function
    def insert(self, word):
            
        if word not in self.words_list: #only for words not already inserted
            self.words_list.append(word)#updates list of all words
            self.word_count += 1 #updates the number of words added
            
        if word == '':
            return  # doesn't insert empty strings into the tree

        self.root = self.insert_character(self.root, word, 0)

    #Helper function for tree visualization
    def _str_helper(self, node, prefix="    ", child=""):
        child = f"{child}:" if child else "" #add the ":" for the childs
        lines = [f"{child} {prefix} char: {node.char}, terminates: {node.end_of_word}"] #structure of each line of the tree

        if node._ls:
            lines.append(self._str_helper(node._ls, prefix + "  ", "_ls")) #looping for left nodes
        if node._eq:
            lines.append(self._str_helper(node._eq, prefix + "  ", "_eq")) #looping for middle nodes
        if node._gt:
            lines.append(self._str_helper(node._gt, prefix + "  ", "_gt")) #looping for right nodes

        return "\n".join(lines) #combines all lines into one string

    #Tree visualization
    def __str__(self):
        if self.root is None:
            return "" #return nothing if tree is empty
        return "terminates: False\n" + self._str_helper(self.root) #starts visualization starting from the root


    #Helper function for search tool
    def search_helper(self, node, word, index):
        if node is None:
            return None #if the node doesn't exist, then the word doesn't either

        char = word[index] #current letter to compare
        
        if char < node.char:
            return self.search_helper(node._ls, word, index) #going to left node
        
        elif char > node.char:
            return self.search_helper(node._gt, word, index) #going to right node
        
        else:
            if index + 1 == len(word):
                return node #return node if last character
            return self.search_helper(node._eq, word, index + 1) #going to middle node

    #Search tool
    def search(self, word, exact=False):
        if word == '':
            return False #empty string are not stored in the tree

        node = self.search_helper(self.root, word, 0) #search for the node matching the last character
        
        if not node:
            return False #if the node doesn't exist, then the word doesn't either

        return True #word found
