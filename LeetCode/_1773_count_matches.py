# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item.
# You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

def countMatches(items, ruleKey, ruleValue):
    ruleOptions = {"type": 0, "color": 1, "name": 2}
    ruleNumber = ruleOptions[ruleKey]
    answer = 0
    for item in items:
        if item[ruleNumber] == ruleValue:
            answer += 1
    return answer


items = [["phone", "blue", "pixel"], ["computer",
                                      "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey, ruleValue = "type", "phone"
print(countMatches(items, ruleKey, ruleValue))
