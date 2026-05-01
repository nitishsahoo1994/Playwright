str="my name is nitish kumar sahoo"

words=str.split(" ")

rev=""
for word in words:
    rev=word+rev


print(rev)