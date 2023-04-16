# COMP1112 Final Exam
# Part2.py
# Name: Dmitry Knyazhevskiy
# Student #: 1203665

#Function splits the string into a list of individual strings, then finds the index of the last string and starting there and going in revers appends the words to a new string
def reverseWords(sentence):
    words = sentence.split()
    i = len(words)-1
    reverse = ''
    while i >= 0:
        reverse += words[i] + ' '
        i = i-1
    print(reverse)

reverseWords("Writing some normal text")
reverseWords("   This is    a test         ")