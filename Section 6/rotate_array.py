# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotateArray(nums, k):
    newArray = []
    ind = 0
    for i in range(len(nums) - k, len(nums)):
        newArray.append(nums[i])
        ind += 1
    for i in range(len(nums)-k):
        newArray.append(nums[i])
        ind += 1
    return newArray


def reverse(nums, left, right):
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1


def rotateArrayInPlace(nums, k):
    if len(nums) == 1:
        return
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)  # reverse whole array
    reverse(nums, 0, k-1)  # reverse first k elements
    reverse(nums, k, len(nums) - 1)  # reverse first k elements


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
#print(rotateArray(arr, k))
rotateArrayInPlace(arr, k)
print(arr)
