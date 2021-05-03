# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The operations are described below:

# "../": Move to the parent folder of the current folder. (If you are already in the main folder,
#         remain in the same folder).
# "./": Remain in the same folder.
# "x/": Move to the child folder named x(This folder is guaranteed to always exist).
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

# The file system starts in the main folder, then the operations in logs are performed.

# Return the minimum number of operations needed to go back to the main folder after the change folder operations.

def minOperations(logs: list[str]) -> int:
    answer = 0
    for op in logs:
        if op == "../":
            if answer:
                answer -= 1
        elif op == "./":
            continue
        else:
            answer += 1
    return answer


def minOperationsWithStack(logs: list[str]) -> int:
    stack = []
    for op in logs:
        if op == "../":
            if stack:
                stack.pop()
        elif op == "./":
            continue
        else:
            stack.append(op)
    return len(stack)


logs = ["d1/", "d2/", "../", "d21/", "./"]
print(minOperations(logs))
print(minOperationsWithStack(logs))
