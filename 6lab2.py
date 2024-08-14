radi = float(input("Please enter radius: "))
hei = float(input("Please enter height: "))
import math
print(f"Volumn for the circular cylinder is: {float(math.pi*radi*radi*hei):.2f}")
print(f"Lateral surface are: {float(2*math.pi*radi*hei):.2f}")
print(f"Total surface area is: {float(2*math.pi*radi*(radi+hei)):.2f}")