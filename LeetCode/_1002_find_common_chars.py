# Given an array A of strings made only from lowercase letters, return a list of all characters
# that show up in all strings within the list(including duplicates).  For example, if a character
#  occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

def commonChars(A: list[str]) -> list[str]:
    hashMapPrev = {}
    hashMapCur = {}
    answer = []
    for c in A[0]:
        if hashMapPrev.get(c) is None:
            hashMapPrev[c] = 1
        else:
            hashMapPrev[c] += 1

    for i in range(1, len(A)):
        string = A[i]
        hashMapCur = {}
        for char in string:
            if hashMapPrev.get(char) is None:
                continue
            else:
                if hashMapCur.get(char) is None:
                    hashMapCur[char] = 1
                else:
                    hashMapCur[char] = min(hashMapPrev.get(
                        char), hashMapCur.get(char)+1)
        hashMapPrev = hashMapCur
    for key in hashMapCur:
        for i in range(hashMapCur[key]):
            answer.append(key)
    return answer


input = ["bella", "label", "roller"]
print(commonChars(input))
