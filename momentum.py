def momentumCalculator(mass, velocity):

    momentum = mass*velocity
    return momentum

m = int(input("Please enter a mass:"))
v = int(input("Please enter a velocity:"))

mo = momentumCalculator(m, v)
print(mo , "Kg/ms")