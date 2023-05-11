import string
import math

"""
Node class that holds letter value, and embedded hash table within itself
"""
class hashNode:
    def __init__(self, value, nested_hash):
        self.size = 26 #size is 26 since there are 26 letters in alphabet
        self.value = value #string value, singular 
        self.nested_hash = nested_hash #nested hash table

    def __str__(self):
        print(self.value)

"""
Node class that holds letter value, and definiton of word at end of hash
"""
class hashNode_def:
    def __init__(self, value, definition):
        self.value = value
        self.definition = definition

"""
Customized hash table that has 3 layers of 26 slots, that holds distinct 
3 letter words and their definitions.
"""
class hashTable:
    """
    Init function to take create hash table based on slots size (26)
    """
    def __init__(self, slots):
        self.slots = slots
        self.top_level = [None] * slots #create top-level list of hashnodes
        for i in range(slots): #populate top level
            topnode = hashNode(None, [None]*slots) #init top node
            self.top_level[i] = topnode
            for j in range(slots): #populate mid level
                mid_node = hashNode(None, [None]*slots) #init mid node
                topnode.nested_hash[j] = mid_node
                for k in range(slots): #populate bottom level with value and definition
                    bot_node = hashNode_def(None, None)
                    mid_node.nested_hash[k] = bot_node

    """
    Insert function to add a word and its definiton into the
    3 layered hash table, only inserts if word is not already in
    hash table.
    """
    def insert(self, word, definition):
        if (self._search(word) == 0): #only inserting if word is not presnt in table
            pos1 = self._custom_hash(word[0]) #initializing hash positions
            pos2 = self._custom_hash(word[1])
            pos3 = self._custom_hash(word[2])
            self.top_level[pos1].value = word[0]
            self.top_level[pos1].nested_hash[pos2].value = word[1]
            self.top_level[pos1].nested_hash[pos2].nested_hash[pos3].value = word[2]
            self.top_level[pos1].nested_hash[pos2].nested_hash[pos3].definition = definition
        
    """
    Delete function.
    """
    def delete(self, word):
        pos1 = self._custom_hash(word[0]) #computing index positions
        pos2 = self._custom_hash(word[1])
        pos3 = self._custom_hash(word[2])
        self.top_level[pos1].nested_hash[pos2].nested_hash[pos3].value = None #only need to clear last letter and definition
        self.top_level[pos1].nested_hash[pos2].nested_hash[pos3].definition = None
    
    """
    Search function to check if 3 letter word exists already in hashtable, to 
    be used by other class functions. Call by passing a self._search(str word).
    """
    def _search(self, word):
        found = 0
        hash1 = self._custom_hash(word[0]) #computing index positions
        hash2 = self._custom_hash(word[1])
        hash3 = self._custom_hash(word[2])
        if self.top_level[hash1].value == word[0]: #first letter is populated
            if self.top_level[hash1].nested_hash[hash2].value == word[1]: #second letter is populated
                if self.top_level[hash1].nested_hash[hash2].nested_hash[hash3].value == word[2]: #third letter is populated
                    found = 1 #all 3 letters are populated, word is already present, update found value
        return found

    """
    Search function to check if 3 letter word exists already in hashtable, to 
    be used by user in main program file.
    """
    def search(self, word):
        found = 0
        definition = None
        hash1 = self._custom_hash(word[0]) #computing index positions
        hash2 = self._custom_hash(word[1])
        hash3 = self._custom_hash(word[2])
        if self.top_level[hash1].value == word[0]: #first letter is populated
            if self.top_level[hash1].nested_hash[hash2].value == word[1]: #second letter is populated
                if self.top_level[hash1].nested_hash[hash2].nested_hash[hash3].value == word[2]: #third letter is populated
                    found = 1 #all 3 letters are populated, word is already present, update found value
                    definition = self.top_level[hash1].nested_hash[hash2].nested_hash[hash3].definition
        
        return found, definition
    
    """
    Custom hash that takes letter as and arg and spits out
    index position for that letter to take, private function.
    """
    def _custom_hash(self, letter):
        return ((ord(letter) + 987 - 17) % 26)

    """
    Function to print list of menu options for main program.
    """
    def options(self):
        print("Here is the list of options you have to interact with the 3 layered hashtable:")
        print("Enter 1 on your keyboard to search the hash table for a 3 letter word")
        print("Enter 2 to insert a valid three letter word and definition into the hashtable")
        print("Enter 3 to delete a letter and its definition from the hashtable")
        print("Enter 4 to end the program")


