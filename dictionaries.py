# Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary using 
# a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print 
# how many messages the person has.

fname = input("File name:")
fhand = open(fname)
ddd = {}

for line in fhand:
    if not line.startswith("From:"):
        continue
    line_list = line.split()
    ddd[line_list[1]] = ddd.get(line_list[1], 0) + 1

bigname = None
bigcount = None
smallname = None
smallcount = None

for i,j in ddd.items():
    if bigcount is None or j > bigcount:
        bigcount = j
        bigname = i

for i,j in ddd.items():
    if smallcount is None or j < smallcount:
        smallcount = j
        smallname = i

print("Max", bigname, bigcount)
print("Min", smallname, smallcount)

