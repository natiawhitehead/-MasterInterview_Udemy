# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
#  Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


def numJewelsInStones(jewels: str, stones: str) -> int:
    hashTable = {}
    answer = 0
    for i in jewels:
        hashTable[i] = True
    for i in stones:
        if hashTable.get(i):
            answer += 1
    return answer


print(numJewelsInStones("aA", "aAAbbbb"))
