top3 = [0, 0, 0] #top 3 elves with cals
tempcal = 0 # Temp value for cals
templine = 0 # Temp line because python hates me

f = open("input.txt", "r")
#loop through everything, if you can't strip it, check the values, this time, check each top3 value and compare it. Else add the values to the tempcal, when your done print the biggest cal.
for line in f:
    if not line.strip():
        if tempcal > top3[0]:
            top3[0] = tempcal
            tempcal = 0
        elif tempcal > top3[1]:
            top3[1] = tempcal
            tempcal = 0
        elif tempcal > top3[2]:
            top3[2] = tempcal
            tempcal = 0
        else:
            print("skipping, temp was smaller! " + str(tempcal) + " .vs " + str(top3))
            top3.sort()
            tempcal = 0
    else:
        templine = line.strip()
        tempcal = int(templine) + tempcal
print(top3)
print(top3[0] + top3[1] + top3[2])