tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90 # tupple can't be changed
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])  # it's basically len(tup)-1
print(tup[2])
# print(tup[34])

if 3421 in tup:
    print("Yes 342 is present in this tuple")
tup2 = tup[1:4]  # slicing in tupple. here new tupple is created.
print(tup2)
