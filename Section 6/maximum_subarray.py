# leetcode #53

def maxSubArray(nums):  # O(n2)
    ans = nums[0]
    for i in range(len(nums)):
        cursum = nums[i]
        ans = max(cursum, ans)
        for j in range(i+1, len(nums)):
            cursum += nums[j]
            ans = max(cursum, ans)
    return ans


def maxSubArrayLiniar(nums):  # O(n) Kadanes Algorithm
    ans = nums[0]
    temp = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > temp + nums[i]:
            temp = nums[i]
        else:
            temp += nums[i]
        ans = max(ans, temp)
    return ans


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(arr))
print(maxSubArrayLiniar(arr))
