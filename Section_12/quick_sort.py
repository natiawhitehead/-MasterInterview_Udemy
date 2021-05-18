def partition(nums, left, right):
    pivot = nums[right]
    greater_index = None
    for i in range(left,right):
        if nums[i] >= pivot and greater_index is None:
            greater_index = i
        elif nums[i] < pivot and greater_index is not None:
            temp = nums[greater_index]
            nums[greater_index] = nums[i]
            nums[i] = temp
            greater_index = min(greater_index + 1, i)
    if greater_index is not None:
        temp = nums[greater_index]
        nums[greater_index] = pivot
        nums[right] = temp
        return greater_index
    else:
        return right

def quicksort(nums,left,right):
    if left < right:
        newIndexOfPivot = partition(nums,left,right)
        quicksort(nums,left,newIndexOfPivot - 1)
        quicksort(nums, newIndexOfPivot + 1, right)
    

numbers = [-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]
quicksort(numbers,0,len(numbers)-1)
print(numbers)
