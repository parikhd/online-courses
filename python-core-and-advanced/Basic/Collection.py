lst = [.5, "String"]
print(lst)
lst.append(100)
print(lst)

# lst.remove(25)  # Exception since 25 is not in list

del (lst[0])
print(lst)
lst = [10, "Dhruv"]
# print(max(lst)) # Exception cannot compare str and int
lst.remove("Dhruv")
print(lst)
lst.insert(4, 100)  # index, value,if index>size then it is appeding
print(lst)

lst = [2, 5, -3, 9, 100, 12]
lst.sort()  # default increasing order
print(lst)
lst.sort(reverse=True)  # descending order
print(lst)

lst = [-200, 200]
print(min(lst))

lst = ["Dhruv", 2]
# print(max(lst))  # Exception cannot compare str and int

lst.clear()
print(lst)  # Empty List

# TUPLE - Immutable List

tpl = (10, 20)
print(tpl[1])
print(max(tpl))

# List to Tuple and vice-versa
tpl = tuple(lst)
print(type(tpl))
lst1 = list(tpl)
print(type(lst1))

# Set
st = {10, 20, 10, 30}
print(st)
# Set does not allow index, subscripting
st.update([45])
print(st)

# Frozen Set - Immutable Set
fst = frozenset(st)
# fst.update([20])  # Exception fozenset has no attribute update

# Bytes
byt = bytes(st);
print(byt)  # b'\n\x14-\x1e'

#BytesArray
byt = bytearray(st)
print(byt)  # bytearray(b'\n\x14-\x1e')

# Dictionary - Hash Table
dct = {1: "one", 2: "two", "three":3}
print(dct.keys())
dct.update({10: "ten"})
print(dct.keys())
print(dct["three"])    # 3
