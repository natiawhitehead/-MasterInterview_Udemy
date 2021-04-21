# Given the array nums consisting of 2n elements in the form[x1, x2, ..., xn, y1, y2, ..., yn].

# Return the array in the form[x1, y1, x2, y2, ..., xn, yn].

def shuffle(nums, n):
    index_left = 0
    index_right = n
    answer = []
    while index_left != n:
        answer.append(nums[index_left])
        answer.append(nums[index_right])
        index_left += 1
        index_right += 1
    return answer


print(shuffle([2, 5, 1, 3, 4, 7], 3))
