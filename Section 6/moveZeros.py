# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in -place without making a copy of the array.
def moveZeros(nums):
    index = -1
    for i in range(len(nums)):
        if nums[i] == 0 and index == -1:
            index = i
        elif index != -1 and nums[i] != 0:
            nums[index] = nums[i]
            index += 1
            nums[i] = 0
    return nums


print(moveZeros([0, 1, 0, 3, 12]))
