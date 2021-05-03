# Given an array target and an integer n. In each iteration, you will read a number from
# list = {1, 2, 3..., n}.

# Build the target array using the following operations:

# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# Return the operations to build the target array. You are guaranteed that the answer is unique.

def buildArray(target: list[int], n: int) -> list[str]:
    answer = []
    ind = 0
    for i in range(1, n+1):
        if ind >= len(target):
            break
        if target[ind] == i:
            answer.append("Push")
            ind += 1
        else:
            answer.append("Push")
            answer.append("Pop")
    return answer


target = [3, 4, 5]
n = 5
print(buildArray(target, n))
