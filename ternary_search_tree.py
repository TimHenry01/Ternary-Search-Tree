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
class TernarySearchTree:
    """
    Ternary Search Tree implementation for efficient string storage and retrieval.
    
    A ternary search tree is a tree data structure where each node has at most three children:
    - left child: stores characters lexicographically smaller than the current node
    - middle child: stores the next character in the current string
    - right child: stores characters lexicographically larger than the current node
    """
    
    def __init__(self):
        """Initialize an empty ternary search tree."""
        self.root = None
        self.word_count = 0

    class Node:
        """Node class for the ternary search tree."""
        def __init__(self, char):
            self.char = char
            self.end_of_word = False  # True if this node marks the end of a word
            self._ls = None  # Left subtree (lesser characters)
            self._eq = None  # Equal subtree (next character in word)
            self._gt = None  # Right subtree (greater characters)

    def insert(self, word):
        """
        Insert a word into the ternary search tree.
        
        Args:
            word (str): The word to insert
            
        Raises:
            ValueError: If word is empty or not a string
        """
        if not isinstance(word, str) or not word:
            raise ValueError("Word must be a non-empty string")
        
        word = word.lower().strip()  # Normalize input
        if not word:
            raise ValueError("Word cannot be empty after normalization")
            
        if not self._contains(word):  # Only insert if word doesn't exist
            self.root = self._insert_recursive(self.root, word, 0)
            self.word_count += 1

    def _insert_recursive(self, node, word, index):
        """
        Recursively insert a word into the tree.
        
        Args:
            node: Current node
            word: Word being inserted
            index: Current character index in the word
            
        Returns:
            Node: The root of the subtree after insertion
        """
        char = word[index]
        
        # Create new node if current node is None
        if node is None:
            node = self.Node(char)
        
        if char < node.char:
            node._ls = self._insert_recursive(node._ls, word, index)
        elif char > node.char:
            node._gt = self._insert_recursive(node._gt, word, index)
        else:  # char == node.char
            if index < len(word) - 1:
                # More characters to process
                node._eq = self._insert_recursive(node._eq, word, index + 1)
            else:
                # End of word
                node.end_of_word = True
        
        return node

    def search(self, word):
        """
        Search for a word in the ternary search tree.
        
        Args:
            word (str): The word to search for
            
        Returns:
            bool: True if word exists, False otherwise
        """
        if not isinstance(word, str) or not word:
            return False
        
        return self._contains(word.lower().strip())

    def _contains(self, word):
        """
        Internal method to check if word exists in the tree.
        
        Args:
            word (str): Normalized word to search for
            
        Returns:
            bool: True if word exists, False otherwise
        """
        return self._search_recursive(self.root, word, 0)

    def _search_recursive(self, node, word, index):
        """
        Recursively search for a word in the tree.
        
        Args:
            node: Current node
            word: Word being searched
            index: Current character index
            
        Returns:
            bool: True if word is found, False otherwise
        """
        if node is None:
            return False
        
        char = word[index]
        
        if char < node.char:
            return self._search_recursive(node._ls, word, index)
        elif char > node.char:
            return self._search_recursive(node._gt, word, index)
        else:  # char == node.char
            if index == len(word) - 1:
                return node.end_of_word
            else:
                return self._search_recursive(node._eq, word, index + 1)

    def delete(self, word):
        """
        Delete a word from the ternary search tree.
        
        Args:
            word (str): The word to delete
            
        Returns:
            bool: True if word was deleted, False if word didn't exist
        """
        if not isinstance(word, str) or not word:
            return False
        
        word = word.lower().strip()
        if not word or not self._contains(word):
            return False
        
        self.root = self._delete_recursive(self.root, word, 0)
        self.word_count -= 1
        return True

    def _delete_recursive(self, node, word, index):
        """
        Recursively delete a word from the tree.
        
        Args:
            node: Current node
            word: Word being deleted
            index: Current character index
            
        Returns:
            Node: The root of the subtree after deletion
        """
        if node is None:
            return None
        
        char = word[index]
        
        if char < node.char:
            node._ls = self._delete_recursive(node._ls, word, index)
        elif char > node.char:
            node._gt = self._delete_recursive(node._gt, word, index)
        else:  # char == node.char
            if index == len(word) - 1:
                node.end_of_word = False
            else:
                node._eq = self._delete_recursive(node._eq, word, index + 1)
        
        # Remove node if it's not useful anymore
        if (not node.end_of_word and 
            node._ls is None and 
            node._eq is None and 
            node._gt is None):
            return None
        
        return node

    def prefix_search(self, prefix):
        """
        Find all words with the given prefix.
        
        Args:
            prefix (str): The prefix to search for
            
        Returns:
            list: List of words with the given prefix
        """
        if not isinstance(prefix, str) or not prefix:
            return []
        
        prefix = prefix.lower().strip()
        if not prefix:
            return []
        
        # Find the node representing the end of the prefix
        prefix_node = self._find_prefix_node(self.root, prefix, 0)
        if prefix_node is None:
            return []
        
        # Collect all words from this node
        results = []
        if prefix_node.end_of_word:
            results.append(prefix)
        
        self._collect_words(prefix_node._eq, prefix, results)
        return sorted(results)

    def _find_prefix_node(self, node, prefix, index):
        """
        Find the node that represents the end of the given prefix.
        
        Args:
            node: Current node
            prefix: Prefix being searched
            index: Current character index
            
        Returns:
            Node: Node representing end of prefix, or None if not found
        """
        if node is None:
            return None
        
        char = prefix[index]
        
        if char < node.char:
            return self._find_prefix_node(node._ls, prefix, index)
        elif char > node.char:
            return self._find_prefix_node(node._gt, prefix, index)
        else:  # char == node.char
            if index == len(prefix) - 1:
                return node
            else:
                return self._find_prefix_node(node._eq, prefix, index + 1)

    def _collect_words(self, node, prefix, results):
        """
        Collect all words from a subtree with the given prefix.
        
        Args:
            node: Root of subtree to collect from
            prefix: Current prefix
            results: List to store results
        """
        if node is None:
            return
        
        # Traverse left subtree
        self._collect_words(node._ls, prefix, results)
        
        # Process current node
        current_word = prefix + node.char
        if node.end_of_word:
            results.append(current_word)
        
        # Traverse equal subtree (continue building word)
        self._collect_words(node._eq, current_word, results)
        
        # Traverse right subtree
        self._collect_words(node._gt, prefix, results)

    def __len__(self):
        """Return the number of words in the tree."""
        return self.word_count

    def all_strings(self):
        """
        Return all words stored in the tree.
        
        Returns:
            list: Sorted list of all words in the tree
        """
        return self.prefix_search("")

    def is_empty(self):
        """
        Check if the tree is empty.
        
        Returns:
            bool: True if tree is empty, False otherwise
        """
        return self.root is None

    def clear(self):
        """Clear all words from the tree."""
        self.root = None
        self.word_count = 0

    def height(self):
        """
        Calculate the height of the tree.
        
        Returns:
            int: Height of the tree (0 for empty tree)
        """
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        """
        Recursively calculate height of subtree.
        
        Args:
            node: Root of subtree
            
        Returns:
            int: Height of subtree
        """
        if node is None:
            return 0
        
        left_height = self._height_recursive(node._ls)
        equal_height = self._height_recursive(node._eq) 
        right_height = self._height_recursive(node._gt)
        
        return 1 + max(left_height, equal_height, right_height)

    def __str__(self):
        """String representation of the tree."""
        if self.is_empty():
            return "Empty Ternary Search Tree"
        return f"Ternary Search Tree with {len(self)} words"

    def __repr__(self):
        """Detailed string representation."""
        return f"TernarySearchTree(words={len(self)}, height={self.height()})"
