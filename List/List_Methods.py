l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))

m = l  # here m is reffering to list 'l'. No new list created in memory
m[0] = 0  # m is changed that's mean 'l' is also changed as it's reference
print(l)

# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m  # list merging
# print(k)
# l.extend(m)
print(l)
