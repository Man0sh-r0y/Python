# string slicing
fruit = "Mango"
mangoLen = len(fruit)  # len() function given length of the string
print(mangoLen)
# print(fruit[0:4]) # it goes from index=0 to index=3
# print(fruit[1:4]) # it goes from index=1 to index=3
# print(fruit[:5]) # it means fruit[0:5]

print(fruit[0:-3])  # it means index goes from 0 to len(fruit)-3
# It means -->
print(fruit[0:len(fruit)-3])  # same as fruit[: len(fruit)-3]

print(fruit[-1:len(fruit) - 3])
# it means index goes from len(fruit)-1 to len(fruit)-3
print(fruit[-3:-1])  # As we know len(fruit)=5
# it means index goes from 2 (=5-3) to 4 (=5-1)

# if we do like this-->
print(fruit[-1:-3])  # it will print nothing
'''As it means index goes from len(fruit)-1 to len(fruit)-3. That's mean
 index is from 4 to 2. It does not make any sense. So no print in console'''

# Quick Quiz:
str = "Harry"  # len(str)=5
print(str[-4:-2])
# it means indexing goes from 1 (=5-4) to 3 (=5-2)
# so 'ar' will be printed
