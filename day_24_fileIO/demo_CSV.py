import csv

login_data=[]
with open('/Users/aaa/IdeaProjects/PythonTrain/PythonTrain/testData/data.csv',newline='',encoding='utf-8') as csvFile:
    reader=csv.DictReader(csvFile)

    for row in reader:
        login_data.append(row['email'])


                         # ,row['password'],row['validity'])
print(type(login_data))
print(login_data)
