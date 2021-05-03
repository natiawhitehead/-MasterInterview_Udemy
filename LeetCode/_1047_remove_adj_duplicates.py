# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent
# and equal letters, and removing them.

# We repeatedly make duplicate removals on S until we no longer can.

# Return the final string after all such duplicate removals have been made.
# It is guaranteed the answer is unique.

def removeDuplicates(S: str) -> str:
    stack = []
    answer = ""
    for c in S:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
    return answer.join(stack)


input = "abbaca"
print(removeDuplicates(input))
