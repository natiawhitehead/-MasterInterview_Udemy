# Given an array of integers nums.

# A pair(i, j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

def numIdenticalPairs(nums):
    answer = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                answer += 1
    return answer


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
