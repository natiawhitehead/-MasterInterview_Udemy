# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def searchRange( nums: list[int], target: int) -> list[int]:
    answer = []

    def binarySearch(FindStart=True):
        left, right = 0, len(nums) - 1
        while left < right:
            if FindStart:
                mid = left + (right - left) // 2
            else:
                mid = left + (right - left + 1) // 2

            if nums[mid] == target:
                if FindStart:
                    right = mid
                else:
                    left = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] == target:
            answer.append(left)
        else:
            answer.append(-1)
            answer.append(-1)

    if len(nums) == 0:
        return [-1, -1]
    binarySearch()
    if len(answer) == 2:
        return answer
    else:
        binarySearch(False)
    return answer


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums,target))
