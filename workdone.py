def workdoneCalculator(force, distancemoved):

    workdone = force*distancemoved
    return workdone

f = int(input("Please enter a force: "))
d = int(input("Please enter a distance moved: "))

wd = workdoneCalculator(f , d)
print ("Work Done is: " , wd , "J")


def kineticenergyCalculator(mass, speed):

    kineticenergy = 0.5*mass*speed
    return kineticenergy

m = int(input("Please enter a mass: "))
s = int(input("Please enter a speed: "))

ke = kineticenergyCalculator(m,s)
print ("Kinetic Energy is: " , ke , "J")