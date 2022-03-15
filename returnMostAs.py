print("This program will accept two DNA strings and return the string with the most A's.")
string1 = input('Please enter DNA string 1: ')
string2 = input('Please enter DNA string 2: ')

aCount1 = 0
aCount2 = 0
invalid = ''

for i in string1:
    if i.upper() == 'A':
        aCount1 += 1

for i in string2:
    if i.upper() == 'A':
        aCount2 += 1

if aCount1 > aCount2:
    print("The string with the most A's is: " + string1)
elif aCount2 > aCount1:
    print("The string with the most A's is: " + string2)
elif aCount1 == aCount2:
    print("The strings contain the same amount of A's.")
