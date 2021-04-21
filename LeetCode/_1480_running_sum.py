# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

def runningSum(nums):
    answer_array = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        answer_array.append(sum)
    return answer_array


print(runningSum([1, 2, 3, 4]))
print(runningSum([1, 1, 1, 1]))
print(runningSum([3, 1, 2, 10, 1]))


# same problem with in place

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


testArray = [1, 2, 3, 4]
runningSum(testArray)
print("In place: ", testArray)
