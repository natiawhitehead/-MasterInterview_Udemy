def selectionSort(nums):
    
    for i in range(len(nums)):
        min = nums[i]
        min_ind = i
        for ind in range(i,len(nums)):
            if nums[ind] < min:
                min = nums[ind]
                min_ind = ind
        temp = nums[i]
        nums[i] = min
        nums[min_ind] = temp


numbers = [1, 54, 6, 7, 12, 9, 0, 31]
selectionSort(numbers)
print(numbers)
