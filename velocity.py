def velocityCalculator(distance, time):
    
    speed = distance*time
    return speed

d = 10
t = 20

s = velocityCalculator(d,t)
print(s , 'm/s')



def accelerationCalculator(velocitychange , timetaken):

    velocitychange = endvelocity - initialvelocity

    endvelocity = 30
    initialvelocity = 10 

    acceleration = velocitychange/timetaken
    return acceleration

v = endvelocity  - initialvelocity
t = 5

a = accelerationCalculator(v,t)
print(a , "m/s2" )