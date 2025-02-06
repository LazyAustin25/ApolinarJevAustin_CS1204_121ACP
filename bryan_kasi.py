import math
dia = int(input("Ano lapad ng bilog mo?: "))
rad = dia/2
sur = 4*math.pi*(rad**2)
vol = (4/3)*math.pi*(rad**3)
print(f"Diameter of the sphere: {dia}")
print("Surface Area is %.4f" % sur)
print("Volume is %.4f" % vol)