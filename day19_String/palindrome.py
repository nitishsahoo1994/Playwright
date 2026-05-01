
str="java"


def reverse(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev



def palindromeCheck(str):
    if reverse(str)==str:
        return True
    else:
        return False


print(palindromeCheck("aba"))


