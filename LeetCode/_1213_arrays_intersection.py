# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
# return a sorted array of only the integers that appeared in all three arrays.

def arraysIntersection(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    hashTable = {}
    answer = []
    for number in arr1:
        hashTable[number] = 0
    for number in arr2:
        if hashTable.get(number) == 0:
            hashTable[number] += 1
    for number in arr3:
        if hashTable.get(number) == 1:
            answer.append(number)
    return answer

# with 3 pointers without extra space


def arraysIntersectionThreePointers(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    pointer1 = pointer2 = pointer3 = 0
    answer = []
    while pointer1 < len(ar1) and pointer2 < len(ar2) and pointer3 < len(ar3):
        if arr1[pointer1] == ar2[pointer2] == ar3[pointer3]:
            answer.append(ar1[pointer1])
            pointer1 += 1
            pointer2 += 1
            pointer3 += 1
        else:
            minInThree = min(ar1[pointer1], ar2[pointer2], ar3[pointer3])
            if ar1[pointer1] == minInThree:
                pointer1 += 1
            if ar2[pointer2] == minInThree:
                pointer2 += 1
            if ar3[pointer3] == minInThree:
                pointer3 += 1
    return answer


ar1 = [1, 2, 3, 4, 5]
ar2 = [1, 2, 5, 7, 9]
ar3 = [1, 3, 4, 5, 8]
print(arraysIntersection(ar1, ar2, ar3))
print(arraysIntersectionThreePointers(ar1, ar2, ar3))
