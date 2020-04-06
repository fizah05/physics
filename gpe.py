def gpeCalculator(mass,gfs,changeinheight):

    gpe = mass*gfs*changeinheight
    return gpe

m = int(input("Please enter a mass: "))
ch = int(input("Please enter a height: "))
gfs = 10

gpe = gpeCalculator(m, gfs, ch)
print("Gravitational Potential Energy is: ", gpe, "J")