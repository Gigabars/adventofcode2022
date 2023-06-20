#Find what letter appears twice per line, split down the middle.
#Add them based on letter count, a = 1, z = 26, A = 27, Z = 52

f = open("input.txt", "r")
val = 0
letterdict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26,
}
for line in f:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:] #Splits lines into 2 splits.
    char = (line.join((set(firstpart).intersection(secondpart)))) #Gets the common char.
    print("---------")
    print("Char is: " + char)
    charlow = char.lower()
    addedval = letterdict[charlow]
    if charlow == char: # checks to see if the charlow and char are the same, if not, adds 26 to the added val (accounts for cap letters.)
        pass
    else:
        addedval += 26
    print("Value: " + str(addedval)) #Prints as number based on value.
    val += addedval
    print("---------")
print(val)