def momentumCalculator(mass, velocity):

    momentum = mass*velocity
    return momentum

m = int(input("Please enter a mass:"))
v = int(input("Please enter a velocity:"))

mo = momentumCalculator(m, v)
print("momentum is: " , mo , "Kg/ms")

def stoppingdistanceCalculator(thinkingdistance, brakingdistance):
    
    stoppingdistance = thinkingdistance + brakingdistance
    return stoppingdistance

td = int(input("Please enter a thinking distance:"))
bd = int(input("Please enter a braking distance:"))

st = stoppingdistanceCalculator(td , bd)
print("Stopping distance is: " , st)