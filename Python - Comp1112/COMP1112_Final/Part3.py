# COMP1112 Final Exam
# Part3.py
# Name: Dmitry Knyazhevskiy
# Student #: 1203665


#Writes all the lines to text file
f = open("data.txt","w+")
f.write("1,2,3,4,5,6,7,8,9,10\n")
f.write("This is a test\n")
f.write("1 2 3 4 5 6 7 8 9 10\n")
f.write("10,9,8,7,6,5,4,3,2,1")
f.close()

#Function called readFile
def readFile(file):
    #Opens the previously created text file in read mode
    f = open(file,"r")
    #Saves each of the lines as an item in a list
    lines = f.readlines()
    #Closes the file
    f.close()

    #Takes the first item in the list of strings, splits it by the comma, iterates through each of the numbers and prints them as an integer
    line1 = lines[0].strip()
    intList = line1.split(',')
    for i in range(len(intList)):
        print(int(intList[i]))


    #Creates a new file called output for writing into, iterates through each character in the second line, if it is not a vowel it saves it to the output file
    f = open("output.txt", "w+")
    line2 = lines[1].strip()
    for letter in line2:
        if(letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u' and letter != 'A' and letter != 'E' and letter != 'I' and letter != 'O' and letter != 'U'):
            f.write(letter)
      

    #Takes the third item in the list of strings, splits it by the space, iterates through each of the numbers and prints them as an integer
    line3 = lines[2].strip()
    intList = line3.split()
    for i in range(len(intList)):
        print(int(intList[i]))

    
    #Takes the fourth item in the list of string, splits it by the comma into a list, sorts that list in descending order returns that list back against as a string
    line4 = lines[3].strip()
    intList = line4.split(',')
    reverseList = sorted(intList, key=int, reverse=True)
    return ', '.join(reverseList)


print(readFile("data.txt"))