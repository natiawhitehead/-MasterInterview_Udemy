# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars(each character can only be used once).

# Return the sum of lengths of all good strings in words.

def countCharacters(words: list[str], chars: str) -> int:
    answer = 0
    initHashTable = {}
    for c in chars:
        if initHashTable.get(c) is None:
            initHashTable[c] = 1
        else:
            initHashTable[c] += 1

    for word in words:
        canBeFormed = True
        hashTable = initHashTable.copy()
        for char in word:
            if hashTable.get(char) is None or hashTable[char] <= 0:
                canBeFormed = False
                break
            else:
                hashTable[char] -= 1
        if canBeFormed:
            answer += len(word)
    return answer


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(countCharacters(words, chars))
