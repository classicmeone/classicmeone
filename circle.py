import math
def circle(rad):
	area = math.pi * rad * rad

	return area

rad = input("Enter radius of circle: ")
rad = int(rad)
print("Area of circle is ",circle(rad))
