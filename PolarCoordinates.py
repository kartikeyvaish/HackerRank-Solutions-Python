import cmath
import math
s=input()
z=complex(s)


r = math.sqrt( (z.real*z.real) + (z.imag * z.imag))
print(r)
print(cmath.phase(complex(z.real, z.imag)))