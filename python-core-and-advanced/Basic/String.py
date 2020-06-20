s = "This is String"
s1 = """
    Test Multi Line
    String
"""
print(s1)
print(s[1])
print(s * 2)
print(len(s))

print(s[0:5])  # This [start index : end index]
print(s[6:])  # s String
print(s[:5])  # This

print(s[-4:-1]) # rin g=-1, n=-2, i=-3, ...

"""
Step Value - defines how many steps to jump in one direction
2 -> jump 2 steps left to right direction
-2 -> jump 2 steps right to left direction
"""


print(s[0:10:2])  # Ti sS ,jump by 2 steps
print(s[10:0:-1])  # rtS si sih
print(s[::1])  # This is String
print(s[::-1]) # gnirtS si sihT


s=" String with Spaces   "
print(s.strip())  # Strip empty spaces on both sides
print(s.lstrip())  # Strip empty spaces on left sides
print(s.rstrip())  # Strip empty spaces on right sides

print(s.find("Spa"))  # Index of occurrence of Spa
print(s.find("Spa",0,5))  # -1 Not Found between 0:5

s1=s.replace("with","of") # Creates a copy does not modify original string like Java
print(s)
print(s1)

print(s.upper())  # STRING WITH SPACES
s1=s.lower() # string with spaces
print(s1.title()) # String With Spaces
print(s.count("S")) # 2
