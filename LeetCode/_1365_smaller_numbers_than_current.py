# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    copyOfNums = nums.copy()
    hashTable = {}
    copyOfNums.sort()
    for i in range(len(nums)):
        if(hashTable.get(copyOfNums[i]) is None):
            hashTable[copyOfNums[i]] = i
    for i in range(len(nums)):
        nums[i] = hashTable.get(nums[i])
    return nums


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
