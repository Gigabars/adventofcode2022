#Find what letter appears twice per line, split down the middle.
#Add them based on letter count, a = 1, z = 26, A = 27, Z = 52
num_lines = sum(1 for _ in open('input.txt'))
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
lines = []
with open("input.txt", 'r') as infile:
    lines = [line.strip() for line in infile] #Load all lines into list.
start = 0
stop = 3
temp = ""
item1 = '0'
item2 = '0'
item3 = '0'
group = 1
while True:
    for item in lines[start:stop]: #Get the next 3 lines.
        if item1 == '0':
            item1 = item
        elif item2 == '0':
            item2 = item
        elif item3 == '0':
            item3 = item
    char = (temp.join((set(item1).intersection(item2).intersection(item3))))
    item1 = '0'
    item2 = '0'
    item3 = '0'
    print("---------")
    print("Char is: " + char)
    print("Group: " + str(group))
    group += 1
    charlow = char.lower()
    addedval = letterdict[charlow]
    if charlow == char: # checks to see if the charlow and char are the same, if not, adds 26 to the added val (accounts for cap letters.)
        pass
    else:
        addedval += 26
    print("Value: " + str(addedval)) #Prints as number based on value.
    val += addedval
    print("---------")
    start += 3 
    stop += 3
    if start == num_lines:
        print(val)
        break