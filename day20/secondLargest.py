mylist=[453,30,987,634,2873,42,382]

large=mylist[0]
slarge=-1


for i in mylist:
    if i > large:
        slarge=large
        large=i
    elif large > i > slarge:
        slarge=i


print(slarge)