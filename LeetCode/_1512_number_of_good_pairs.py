# Given an array of integers nums.

# A pair(i, j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

def numIdenticalPairs(nums: list[int]) -> int:
    hashTable = {}
    answer = 0
    for i in nums:
        if hashTable.get(i) is None:
            hashTable[i] = 1
        else:
            answer += hashTable[i]
            hashTable[i] += 1
    return answer


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
