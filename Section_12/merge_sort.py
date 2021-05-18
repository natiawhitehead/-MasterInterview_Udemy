def mergeSort(nums,left,right):
    if left == right:
        return [nums[left]]
    mid = (left + right) // 2
    left = mergeSort(nums, left, mid)
    right = mergeSort(nums,mid + 1, right)
    l_ind = 0
    r_ind = 0
    newArr = []
    while l_ind < len(left) or r_ind < len(right):
        if l_ind == len(left):
            newArr.append(right[r_ind])
            r_ind += 1  
        elif r_ind == len(right):
            newArr.append(left[l_ind])
            l_ind += 1
        elif left[l_ind] < right[r_ind]:
            newArr.append(left[l_ind])
            l_ind += 1
        else:
            newArr.append(right[r_ind])
            r_ind += 1
    return newArr


numbers = [1, 54, 6, 7, 12, 9, 0, 31]
newarr = mergeSort(numbers,0,len(numbers)-1)
print(newarr)


    

