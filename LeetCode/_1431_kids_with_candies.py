# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or
# she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

def kidsWithCandies(candies, extraCandies):
    max = 0
    answer = []
    for i in candies:
        if max < i:
            max = i
    for candy in candies:
        answer.append(candy + extraCandies >= max)
    return answer


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
