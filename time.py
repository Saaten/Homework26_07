'''ներմուծվածին ավելացրած ժամը am pm -ով '''
hour=float(input("Enter hour: "))
if hour>12:
    print("Error")
else:
    time=int(input('AM(0) or PM(1)'))
    f=int(input('how many hours ahead?'))
    planned_hour=int(hour+f)
    while planned_hour>12:
        if time:
            time=0
        else:
            time+=1
        planned_hour-=12
    if time:
        print("New hour: ",planned_hour, "PM ")
    else:
        print("New hour: ", planned_hour, "AM")
