def velocityCalculator(distance, time):
    
    speed = distance*time
    return speed

d = int(input("Enter a distance: "))
t = int(input("Enter a time: "))

s = velocityCalculator(d,t)
print(s , 'm/s')



def accelerationCalculator( finalvelocity, initialvelocity , timetaken):
    
    velocitychange = finalvelocity - initialvelocity
    acceleration = velocitychange/timetaken
    return acceleration
    
f = int(input("Enter a final velocity: "))
i= int(input("Enter an initial velocity: "))
tt = int(input("Enter a time: "))

a = accelerationCalculator(f,i,tt)
print(a , "m/s2" )



def accelerationCalculatordistancebased(finalvelocity,initialvelocity,distance):

    acceleration2 = (finalvelocity*finalvelocity - initialvelocity*initialvelocity)/ 2*distance
    return acceleration2

f2 = int(input("Enter a final velocity: "))
i2 = int(input("Enter an initial velocity: "))
d2 = int(input("Enter a distance: "))

a2 = accelerationCalculatordistancebased(f2,i2,d2)
print(a2 , "m/s2")

if a2 < 0:
    print("The object is decelerating ")

else:
    print("The object is accelerating") 
