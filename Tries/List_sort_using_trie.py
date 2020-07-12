from CodeBreakers.Data_structures_interview.Tries.Trie import Trie
from CodeBreakers.Data_structures_interview.Tries.TrieNode import TrieNode
# Recursive Function to generate all words in alphabetic order


def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if (root.is_end_word):
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if (root.children[i] is not None):
            # Non-null child, so add that index to the character array
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(arr):
    result = []

    # Creating Trie and Inserting words from array
    trie = Trie()
    for x in range(len(arr)):
        trie.insert(arr[x])

    word = [''] * 20
    get_words(trie.get_root(), result, 0, word)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
print(sort_list(keys))
