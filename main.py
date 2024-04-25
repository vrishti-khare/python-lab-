# built-in math module
print(abs(-25))
print(pow(2,4))
print(min(10,20,30,40,50))
print(max(10,20,30,40,50))
print(divmod(17,3))
print(bin(64),oct(64),hex(64))
print(round(2.567),round(2.5678,2))

#mathematical functions from maths module
import math
x=1.5375
print(math.pi,math.e)
print(math.sqrt(x))
print(math.factorial(6))
print(math.fabs(x))
print(math.log(x))
print(math.log10(x))
print(math.exp(x))
print(math.trunc(x))
print(math.floor(x))
print(math.ceil(x))
print(math.trunc(-x))
print(math.floor(-x))
print(math.ceil(-x))
print(math.modf(x))

s = "Bamboozled"
#extract B a
print(s[0]),s[1]
print(s[-10],s[-9])
#extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8])
# extract Bamboo
print(s[0:6])
print(s[-6:])
print(s[-10:4])
print(s[:-4])
# reverse bamboozled
print([-1])

print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:3])
print(s[0:10:4])

s=s+'HYPE'
print(s)
s=s[:6]+'Monger'+ s[-1]
print(s)

#the driver should be insured or not
ms =input('enter martial status:')
s = input ('enter sex:')
age =int(input('enter age:'))
if (ms == 'm') or (ms == 'u' and s == 'm' and age>30)\
    or(ms == 'u' and s == 'f' and age>25):
    print('insured')
else:
    print('not insured')

#WAP that prints all unique combination of 1,2 and 3
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i == j or j == k or k == i:
                k += 1
                continue
            else:
                print(i, j, k)
            k += 1
        j += 1
    i += 1

# WAP to print square root and cube roots  from 1 to 10
import math
width =10
precision = 4
for n in range(1,10):
    s=math.sqrt(n)
    c=math.pow(n,1/3)
    print(f'{n^5}{s:{width}.{precision}}{c:{width}.{precision}}')

# Perform the following operations on a list names
# create a list of 5 names
names=['Anil','Amol','Aditya','Avi','Alka']
print(names)
#insert a name 'Anuj before aditya'
names.insert(2,'Anuj')
print(names)
#append a name 'Zulu'
names.append('Zulu')
print(names)
# replace 'Anil with' 'Anilkumar'
i= names.index('Anil')
names[i] ='Anilkumar'
print(names)
#sort all the names in the list
names.sort()
print(names)
#print revered sorted list
names.reverse()
print(names)


import random
# Generate a set containing 10 random numbers in the range of 15 to 45
random_numbers_set = set()
while len(random_numbers_set) < 10:
    random_number = random.randint(15, 45)
    random_numbers_set.add(random_number)

print("Original set of random numbers:", random_numbers_set)

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers_set if num < 30)
print("Count of numbers less than 30:", count_less_than_30)



# Delete all the numbers less than 30 from the set
random_numbers_set = {num for num in random_numbers_set if num >= 30}

print("Set after deleting numbers less than 30:", random_numbers_set)

#WAP to merge the two dictionaries into third dictionary
boys ={'Nilesh': 41,'Aditya':42,'Ravi':47}
girls={'Rashika':38,'Nandani':43,'Rashika':45}
combined ={*boys,*girls}
print(combined)
combined ={*boys,*girls}
print(combined)

#WAP to create a calender in Python
import calendar
def create_calendar(year, month):
    # Using the calendar module to generate the calendar for the given year and month
    cal = calendar.month(year, month)
    return cal


if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    print("\nCalendar:")
    print(create_calendar(year, month))


    #WAP to calculate and print paper sizes A0,A1,A2.....A8 using recursion
    def papersizes(i, n, l, b):
        if n!= 0:
            print(f'A{i}: L={int(l)}B= {int(b)}')
            newb =l/2
            newl =b
            n -=1
            i +=1
            papersizes(i, n, newl, newb)
else:
    pass
papersizes(0,7,1189,841)

#WAP that determines whether two objects are of same types whether their situations are same type whether their attributes are same and whether they are pointing to same object
class MyClass:
    def _init_(self, name):
        self.name = name
# Function to determine if two objects have the same type, attributes, and memory address
def compare_objects(obj1, obj2):
    # Check if objects are of the same type
    type_same = type(obj1) == type(obj2)
    attrs_same = vars(obj1) == vars(obj2)
    same_object = obj1 is obj2
    return type_same, attrs_same, same_object
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = obj1
    print("Object 1:", obj1)
    print("Object 2:", obj2)
    print("Object 3:", obj3)
    type_same, attrs_same, same_object = compare_objects(obj1, obj2)
    print("\nAre obj1 and obj2 of the same type?", type_same)
    print("Do obj1 and obj2 have the same attributes?", attrs_same)
    print("Are obj1 and obj2 pointing to the same object?", same_object)
    type_same, attrs_same, same_object = compare_objects(obj1, obj3)
    print("\nAre obj1 and obj3 of the same type?", type_same)
    print("Do obj1 and obj3 have the same attributes?", attrs_same)
    print("Are obj1 and obj3 pointing to the same object?", same_object)


# use of filter function
def fun(n):
    if n%5 == 0:
        return True
    else:
        return False
lst1 = ['A','X','Y','3','M','4','D']
f1 = filter(str.isalpha,lst1)
print(list(f1))
lst2 = [5,18,10,6]
f2 = filter(fun,lst2)
print(list(f2))

# use of reduce() function
from functools import reduce
def getsum(x,y):
    return x+y
def getprod(x,y):
    return x*y
lst = [1,2,3,4,5]
s = reduce(getsum,lst)
p = reduce(getprod,lst)
print(s)
print(p)