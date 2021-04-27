# Given words first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.

# For each such occurrence, add "third" to the answer, and return the answer.

def findOcurrences(text: str, first: str, second: str) -> list[str]:
    wordsArray = text.split(" ")
    hashTable = {}
    answer = []
    for i in range(len(wordsArray)):
        word = wordsArray[i]
        if hashTable.get(word) is None:
            hashTable[word] = [i]
        else:
            hashTable[word].append(i)
    indicesOfFirst = hashTable[first]
    for i in indicesOfFirst:
        if i == len(wordsArray) - 1:
            continue
        else:
            if wordsArray[i+1] == second and i+2 < len(wordsArray):
                answer.append(wordsArray[i+2])
    return answer


text = "alice is a good girl she is a good student"
first = "a"
second = "good"

print(findOcurrences(text, first, second))
