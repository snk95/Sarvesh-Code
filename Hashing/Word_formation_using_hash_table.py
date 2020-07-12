from CodeBreakers.Data_structures_interview.Hashing.Hashtable import HashTable

# Note: The solution only works for two words and not more.
def is_formation_possible(lst, word):
    if len(word) < 2 or len(lst) < 2:
        return False

    hash_table = HashTable()
    for elem in lst:
        hash_table.insert(elem, True)

    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        if hash_table.search(first) is not None:
            check1 = True
        if hash_table.search(second) is not None:
            check2 = True

        # Return True If both substrings are present in the trie
        if check1 and check2:
            return True

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
