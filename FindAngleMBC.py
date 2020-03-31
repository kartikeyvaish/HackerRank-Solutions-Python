import math
AB = int(input())
BC = int(input())
AC = math.sqrt((AB*AB) + (BC*BC))
AC = AC/2
AB = AB/2
CosX = (math.sqrt((AC*AC) - (AB*AB))) / AC
X = math.acos(CosX)
print(str(int(round(math.degrees(X)))), end="")
print("°")