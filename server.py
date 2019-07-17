import math 
def print_volume(r):
    volume_of_sphere = 4/(3*math.pi*r*3)
    print(volume_of_sphere)

print_volume(5)
print_volume(10)
print_volume(15)

def callMe(my_name):
    print(my_name * 5)

callMe("Frank ")
callMe("mary ")
callMe("John ")