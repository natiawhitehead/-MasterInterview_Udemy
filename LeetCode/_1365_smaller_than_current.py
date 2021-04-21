# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is , for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    answer = []
    for i in range(len(nums)):
        temp = 0
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[j] < nums[i]:
                temp += 1
        answer.append(temp)
    return answer


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
