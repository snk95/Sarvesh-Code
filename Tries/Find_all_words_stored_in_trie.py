from CodeBreakers.Data_structures_interview.Tries.Trie import Trie
from CodeBreakers.Data_structures_interview.Tries.TrieNode import TrieNode


# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
# get_root => trie.get_root()
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)
# Recursive Function to generate all words
def get_words(root, result, level, word):

    # Leaf denotes end of a word
    if root.is_end_word:
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Non-None child, so add that index to the character array
            word[level] = chr(i + ord('a'))  # Add character for the level
            get_words(root.children[i], result, level + 1, word)


def find_words(root):
    result = []
    word = [None] * 20  # assuming max level is 20

    get_words(root, result, 0, word)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
t = Trie()
for i in range(len(keys)):
    t.insert(keys[i])
lst = find_words(t.root)
print(str(lst))
