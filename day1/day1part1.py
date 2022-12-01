biggestcal = 0 # Biggest value
tempcal = 0 # Temp value for cals
templine = 0 # Temp line because python hates me

f = open("input.txt", "r")
# loop through everything, if you can't strip it, check the values, else add the values to the tempcal, when your done print the biggest cal.
for line in f:
    if not line.strip():
        if tempcal > biggestcal:
            biggestcal = tempcal
            tempcal = 0
        else:
            print("skipping, temp was smaller! " + str(tempcal) + " .vs " + str(biggestcal))
            tempcal = 0
    else:
        templine = line.strip()
        tempcal = int(templine) + tempcal
print(biggestcal)