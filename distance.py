x1 ,y1 = input("Enter Coordinates of first point:").split()

x2 ,y2 = input("Enter Coordinates of second point:").split()

distance = ((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2)**0.5
print("Distance is %f"%distance)
