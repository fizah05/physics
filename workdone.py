def workdoneCalculator(force, distancemoved):

    workdone = force*distancemoved
    return workdone

f = int(input("Please enter a force: "))
d = int(input("Please enter a distance moved: "))

wd = workdoneCalculator(f , d)
print ("Work Done is: " , wd , "J")