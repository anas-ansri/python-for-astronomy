import sys

file = open(sys.argv[1])

lines = file.read().splitlines()



sum = 0
n = 0

for i in range( 1, len(lines)):
    numbers = lines[i].split(",")
    for num in numbers:
        sum += int(num)
        n += 1
    
print("Average of all numbers is : ", sum/n)
