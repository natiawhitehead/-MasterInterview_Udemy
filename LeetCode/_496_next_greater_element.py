# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
#  If it does not exist, return -1 for this number.

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    hashTable = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            hashTable[stack.pop()] = num
        if not hashTable.get(num):
            hashTable[num] = -1
        stack.append(num)
    answer = []
    for i in range(len(nums1)):
        answer.append(hashTable[nums1[i]])
    return answer


arr1 = [4, 1, 2]
arr2 = [1, 3, 4, 2]
print(nextGreaterElement(arr1, arr2))
