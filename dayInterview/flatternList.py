def flatten(lst):
    result=[]

    for item in lst:
        if type(item) == list:
            for val in flatten(item):
                result.append(val)
        else:
            result.append(item)

    return result

data = [1, [2, [3, 4], 5], 6]

print(flatten(data))