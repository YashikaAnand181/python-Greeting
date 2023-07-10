
#-----program to greet according to time-----
import time
ts=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print("----Welcome----")
hour=int(input("Enter the hour:"))
if (hour>=0 and hour<12):
    print("Good Morning Sir!")
elif (hour>=12 and hour<16):
    print("Good Afternoon Sir!")
elif (hour >= 16 and hour<20):
    print("Good Evening Sir!")
elif (hour>=20 and hour<24):
    print("Good Night Sir!")
else:
    print("Stay Happy :)")
