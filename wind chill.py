t=int(input("enter the temperature"))
v=int(input("enter the speed of wind"))
wc= (13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16)
print("the wind chill is:",wc)      
