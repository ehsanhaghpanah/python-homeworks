
from decimal import DivisionByZero

def foo(a: float, b: float) -> float:
     try:
          xa = a ** 0.5
          xb = b ** 0.5
          return a / b
     except DivisionByZero:
          print("b must be non zero")
     except TypeError:
          print("a and b must be float numbers")
     except:
          print("error")
          return None

a = input("a = ")
b = input("b = ")

print(foo(a, b))

# a = -1.0
# b = a ** 0.5
# print(b)