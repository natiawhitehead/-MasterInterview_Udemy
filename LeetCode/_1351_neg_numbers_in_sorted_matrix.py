# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
# return the number of negative numbers in grid.

def binarySearch(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= 0:
            left = mid + 1
        else:
            right = mid
    if nums[left] < 0:
        return len(nums) - left
    else:
        return 0

def countNegatives(grid: list[list[int]]) -> int:
    answer = 0
    for row in grid:
        answer += binarySearch(row)
    return answer


input = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(input))
