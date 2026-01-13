
'''
day=8
match day:
    case 1:print("monday")
    case 2:print("tuesday")
    case 3:print("wednesday")
    case 4:print("Thrusday")
    case 5:print("friday")
    case _:print("invalid date")
'''

day=5
match day:
    case 2|3|4|5|6:print("weekdays")
    case 1|7:   print("weekend")
    case _: print("invalid days")