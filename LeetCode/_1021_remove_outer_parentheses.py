# A valid parentheses string is either empty(""), "(" + A + ")", or A + B, where A and B are valid parentheses
# strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all
# valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it
#  into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
#  where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.


def removeOuterParentheses(S: str) -> str:
    stack = []
    answer = ""
    for p in S:
        if p == "(":
            if len(stack) > 0:
                answer += p
            stack.append(p)
        else:
            stack.pop()
            if len(stack) > 0:
                answer += p
    return answer


input = "(()())(())"
print(removeOuterParentheses(input))