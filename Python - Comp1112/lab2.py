'''
for i in range(4):
    print(i)
    


for DmitryIsCool in "Hello Class":
    print(DmitryIsCool, end = "")

x = "myVar"
print(x)



for x in "Hello Class":
    print(x, end = "")

print(x)



for letter in range(4):
    print(letter, end = "")

print(letter)



for letter in "Hello":
    print(letter, end = "")
    print("test loop")  
    print("test outer")
print(letter)



import math

# Get Area from User as Float
area = input("Enter the area: ")

# If Area is Valid
if area > 0:
    # Calculate Radius
    radius = math.sqrt()
    #Return Result to Terminal
    print("The radius is ", radius)

#Error: Invalid Area
else:
    print("Err: Area must be greater than 0")



number = int(input("Etner the numberic grade: "))

if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'

print("The letter grade is ", letter)



number = int(input("Etner the numberic grade: "))

if number >= 0 and number <= 100:
    print("Valid Grade")
else:
    print("ERR: Invalid Grade")



if not(False):
    print("If Statement Entered")

if False or True:
    print("If Statement Entered")



sum - 0.0

data = input("Enter a number, or Q to quit: ")

while data != 'Q':
    number = float(data)

    sum += number

    print("The sum is ", sum)
    data = input("Enter a number, or Q to quit: ")

print("--Loop Exit--")
print("The sum is ", sum)



sum = 0
while True:
    sum += 1
    print(sum)
'''


while True:
    number = int(input("Enter Numberic Grade"))
    if number >= 0 and number <= 100:
        break
    else:
        print("ERR: Invalid Grade")

print("THe valid grade is", number)



while True:
    number = int(input("Enter Numberic Grade"))
    if number >= 0 and number <= 100:
        if number > 89:
            letter = 'A'
        elif number > 79:
            letter = 'B'
    else:
        print("ERR: Invalid Grade")

print("The valid grade is", number)