def reverse(stringToReverse):
    arr = list(stringToReverse)
    left = 0
    right = len(stringToReverse) - 1
    print(left, right)
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return "".join(arr)


print(reverse("Hello my name is Natia"))
