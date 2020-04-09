def gpeCalculator(mass,gfs,changeinheight):

    gpe = mass*gfs*changeinheight
    return gpe

m = int(input("Please enter a mass: "))
ch1 = int(input("Please enter an initial height: "))
ch2 = int(input("Please enter a final height: "))
gfs = 10

ch = ch2 - ch1

gpe = gpeCalculator(m, gfs, ch)
print("Gravitational Potential Energy is: ", gpe, "J")


