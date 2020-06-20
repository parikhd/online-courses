"""
    Author: Dhruv Parikh
"""
# Printing Python version
import sys

print(sys.version)

# DataTypes

a = 10
b = 10.1
print(type(a), type(b))  # int float

c = 0b1001  # Binary
print(c)
print(type(c))

d = 0xF0  # Hexadecimal
print(d)
print(type(d))  # int

e = 0o07  # Octal
print(e)

f = hex(16)
print(f)

g = "13.5"
print(float(g))

a = 9999999999999999999999999999999
print(a + 1)
