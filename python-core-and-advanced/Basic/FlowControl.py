a = 0
if a <= 0:
    print("{} Neither Even Nor Odd".format(a))
elif a % 2 == 0:
    print("EVEN")
    print("Hello")
else:
    print("ODD")

while a <= 20:
    print(a)
    a += 1

print("Odd nos.between a range")

start = 1
end = 10
i = start
while i <= end:
    if i % 2 != 0:
        print(i)
    i += 1

print("Break Demo")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("Continue Demo")
for i in range(1, 20):
    if i % 3 == 0:
        continue
    print(i)
