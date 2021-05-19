# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

def intersection( nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) > len(nums2):
        short, long = nums2, nums1
    else:
        short, long = nums1, nums2
    answerHash = {}
    answer = []
    long.sort()

    def binarySearch(target):
        left, right = 0, len(long) - 1
        while left <= right:
            mid = (left + right) // 2
            if long[mid] == target:
                answerHash[target] = True
                answer.append(target)
                break
            elif long[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    for i in range(len(short)):
        if answerHash.get(short[i]) is None:
            binarySearch(short[i])
    return answer


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print (intersection(nums1,nums2))