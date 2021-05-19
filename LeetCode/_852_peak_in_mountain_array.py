# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

def peakIndexInMountainArray(arr: list[int]) -> int:
    def binarySearch(left, right):
        while left < right:
            mid = left + (right - left + 1) // 2
            if arr[mid] > arr[mid-1]:
                left = mid
            else:
                right = mid - 1
        return left
    return binarySearch(1, len(arr) - 2)


arr = [0, 10, 5, 2]
print(peakIndexInMountainArray(arr))