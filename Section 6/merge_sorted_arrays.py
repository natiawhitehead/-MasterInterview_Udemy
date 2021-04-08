def merge(nums1, m, nums2, n):

    it1 = m-1
    it2 = n-1
    index = len(nums1) - 1
    while it2 >= 0:
        if it1 != -1 and nums1[it1] >= nums2[it2]:
            nums1[index] = nums1[it1]
            it1 -= 1
        else:
            nums1[index] = nums2[it2]
            it2 -= 1
        index -= 1


ar1 = [1, 2, 3, 0, 0, 0]
ar2 = [4, 5, 6]
merge(ar1, 3, ar2, 3)
print(ar1)
