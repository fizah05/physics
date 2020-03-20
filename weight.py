def weightCalculator(mass, gravitationalfieldstrength):

    weight = mass*gravitationalfieldstrength
    return weight

m = int(input("Please enter a mass: "))
gfs = 10

w = weightCalculator(m , gfs)
print (w , "N")



def forceCalculator(mass, acceleration)

    force = mass*acceleration
    return force

m = int(input("Please enter a mass: "))
a = int(input("Please enter an acceleration: "))

f = forceCalculator(m , a)
print (f , "N")