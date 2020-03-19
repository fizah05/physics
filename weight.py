def weightCalculator(mass, gravitationalfieldstrength):

    weight = mass*gravitationalfieldstrength
    return weight

m = int(input("Please enter a mass: "))
gfs = 10

w = weightCalculator(m , gfs)
print (w , "N")