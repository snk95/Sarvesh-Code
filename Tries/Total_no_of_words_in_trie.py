from CodeBreakers.Data_structures_interview.Tries.Trie import Trie
from CodeBreakers.Data_structures_interview.Tries.TrieNode import TrieNode


def total_words(root):
    result = 0

    # Leaf denotes end of a word
    if root.is_end_word:
        result += 1

    for i in range(26):
        # Check if the node has children
        if root.children[i] is not None:
            # Recursively return the word count
            result += total_words(root.children[i])
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(total_words(trie.root))

