# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts.
#  The richest customer is the customer that has the maximum wealth.

def maximumWealth(accounts):
    answer = 0
    for i in range(len(accounts)):
        temp = 0
        for j in range(len(accounts[i])):
            temp += accounts[i][j]
        answer = max(answer, temp)
    return answer


print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
