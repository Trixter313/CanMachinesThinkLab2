from random import *

string_length = int(random() * 100)
outputString = ''

while string_length != int(random()*100):
    letterPicker = random()
    if letterPicker <= .25:
        outputString = outputString + 'A'
    elif .25 < letterPicker <= .5:
        outputString = outputString + 'C'
    elif .5 < letterPicker <= .75:
        outputString = outputString + 'G'
    elif .75 < letterPicker <= 1:
        outputString = outputString + 'T'

print(outputString)