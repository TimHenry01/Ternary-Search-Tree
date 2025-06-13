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
            self.end_of_word = False #False when the letter is the end of the word, True otherwise
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
