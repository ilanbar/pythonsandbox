
import mpmath
mpmath.mp.dps = 50

class _complex:
    def __init__(self, real, imaginary):
        self.real      = real
        self.imaginary = imaginary
    
    def __str__(self):
        sign = '+'
        if self.imaginary < 0:
            sign = ''
        return f'({self.real}{sign}{self.imaginary}j)'

    def __add__(self, other):
        return _complex(self.real + other.real,  self.imaginary + other.imaginary )

    def __sub__(self, other):
        return _complex(self.real - other.real,  self.imaginary - other.imaginary )

    def __mul__(self, other):
        return _complex( self.real * other.real - self.imaginary * other.imaginary, 
                         self.real * other.imaginary + other.real * self.imaginary )

    def __invert__(self ):
        return _complex( self.real, -self.imaginary)

    def __truediv__(self, other):
        real = (self.real * other.real + self.imaginary * other.imaginary) / (other.real**2 + other.imaginary ** 2)
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (other.real**2 + other.imaginary ** 2)
        return _complex(real, imaginary)

    def __abs__(self):
        return _complex(abs(self.real), abs(self.imaginary))

def fib(a,b,n):
    for _ in range(n):
        sum = _complex(1,0)/a + _complex(1,0)/b
        a = b
        b = sum
    return sum


# for i in range(-1000,1000,10):
#     for j in range(-1000,1000,10):
#         a = _complex(mpmath.mpf(1), mpmath.mpf(i))
#         b = _complex(mpmath.mpf(1), mpmath.mpf(j))
#         f = fib(a,b,2000)
#         print(f)

# sqrt = _complex(mpmath.mpf(mpmath.sqrt(2)),0)
a = _complex(mpmath.mpf(1), mpmath.mpf(mpmath.sqrt(2)))
b = _complex(mpmath.mpf(1), mpmath.mpf(mpmath.sqrt(2)))

print(fib(a,b,1000))