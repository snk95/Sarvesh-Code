from CodeBreakers.Data_structures_interview.Tries.Trie import Trie
from CodeBreakers.Data_structures_interview.Tries.TrieNode import TrieNode

def is_formation_possible(dct, word):
    # Create Trie and insert dctionary elements in it
    trie = Trie()
    for x in range(len(dct)):
        trie.insert(dct[x])

    # Get Root
    current_node = trie.root

    # Iterate all the letters of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])

        # if the prefix of word does not exist, word would not either
        if current_node.children[char] is None:
            return False

        # if the substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return true
        elif current_node.children[char].is_end_word:

            if trie.search(word[i + 1:]):
                return True

        current_node = current_node.children[char]

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
