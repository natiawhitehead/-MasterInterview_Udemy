def bubbleSort(nums):
    for i in range(len(nums)):
        for ind in range(len(nums)-1):
            if nums[ind] > nums[ind+1]:
                tmp = nums[ind]
                nums[ind] = nums[ind+1]
                nums[ind+1] = tmp
    
numbers = [1,54,6,7,12,9,0,31]
bubbleSort(numbers)
print(numbers)
