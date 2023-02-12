
print("A","B","C", sep="-")#instead of spaces between entries uses dashes as the separator

def greet(name):
    print("Hello " + name, end="-")#optional argument to add something to the end
    print("This is my function")

greet("Bob")
'''
#can get the length of strings
x = len("Bob")
print(x)

#can get the length of dictionary
y = len({1:1, 2:2, 3:3})
print(y)

def multiplyByTen(number):
    answer = number * 10
    return answer

n = 30
z = multiplyByTen(n)
print("z = ", z)
print("n = ", n)
'''

myInt = 90 #globalscoped variables can be accessed within functions

def multiplyByAny(number, mult):
    answer = number * mult
    global myInt #edit a global variable from inside the local scope
    myInt = 40 
    return answer

n = 30
z = multiplyByAny(n, 2)
print("z = ", z)
print("n = ", n)

#MAPPING
words = ["100", "202","322"]
print(list(map(int, words))) #map applies a function to an array
print("words = ", words)


#FILTERING
#Enters all the entries into the function and only returns the ones that are true
nums = [1,2,3,4,5,6,7]

def even(n):
   # if n % 2 == 0:
      #  return True
    #else:
     #   return False

    #Equivalent to above if else statement
    return n % 2 == 0

filteredNums = []
for num in nums:
    if even(num):
        filteredNums.append(num)

#Filter statement equivalent to above for loop
print(list(filter(even, nums)))


#REDUCING
#Reduces a list a list of values to a single value
def myHighOrder(func, list):#Example 
    for item in list:
        value += func(item)

def add(x,y):
    return x + y

def mult(x,y):
    return x * y

def multIfEven(x, y):
    if even(x) and even(y):
        return x * y
    else:
        return x
from functools import reduce
print(reduce(add, range(10)))

print("Add: ", reduce(add, range(10)))
print("Mult: ", reduce(mult, range(1,11)))
print("MultIfEven: ", reduce(multIfEven, range(1,11)))


#LAMBDA 
#Anonymous function, has no name
print("Add: ", reduce(lambda x,y: x + y, range(10)))
print(list(filter(lambda n: n % 2 == 0, nums)))


#Sorting a Dict
gradeDict = {"Alice": 60, "Bob": 94, "Carl": 80}
print(list(gradeDict.items()))


#String Formatting
name = "Dmitry"
age = "28"
print("My name is " + name + " and my age is " + age)
print(f"My name is {name} and my age is {age}, that times two is {int(age) *2}")

