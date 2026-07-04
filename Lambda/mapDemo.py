numbers=[1,2,3,4,5,6,7]

#map
# res=map(lambda x:x*2,numbers)



#filter
#res=filter(lambda x:x%2==0,numbers)


#sorted by second element
# students=[('Ram',70),
#           ('Abhinav',45),
#           ('Shilu',40)]
#
# print(sorted(students,key=lambda x:x[1]))


#dict sorting
# students ={"Ram":70,'Abhinav':45,'Shilu':40}
# res=sorted(students.items(),key=lambda x:x[0])
# print(res)

#conditional

check = lambda x : 'Even' if x%2==0   else 'odd'
print(check(99))