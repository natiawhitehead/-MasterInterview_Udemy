# Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

# We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

# These lists A and B may contain duplicates. If there are multiple answers, output any of them.

def anagramMappings(A: list[int], B: list[int]) -> list[int]:
    hashTable = {}
    answer = []
    for i in range(len(B)):
        hashTable[B[i]] = i
    for num in A:
        answer.append(hashTable[num])
    return answer


ar1 = [12, 28, 46, 32, 50]
ar2 = [50, 12, 32, 46, 28]
print(anagramMappings(ar1, ar2))
