# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    firstCivils = []

    def binarySearch(nums, i, left, right):
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == 0:
                right = mid
            else:
                left = mid + 1
        if nums[left] == 1:
            firstCivils.append((len(nums), i))
        else:
            firstCivils.append((left, i))

    for i in range(len(mat)):
        binarySearch(mat[i], i, 0,len(mat[i])-1)

    answer = []
    sortedList = sorted(firstCivils, key = lambda x: x[0])
    i = 0
    while k > 0:
        answer.append(sortedList[i][1])
        i += 1
        k -= 1
    return answer


mat =[[1, 1, 0, 0, 0],
 [1, 1, 1, 1, 0],
 [1, 0, 0, 0, 0],
 [1, 1, 0, 0, 0],
 [1, 1, 1, 1, 1]]
k = 3
print(kWeakestRows(mat,k))