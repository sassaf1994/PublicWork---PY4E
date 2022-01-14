# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 

fname = input("File name:")
fhand = open(fname)
characters = {}

fhand_char = fhand.read()
for letter in fhand_char:
    if letter.isalpha() is False:
        continue
    l_letter = letter.lower()
    characters[l_letter] = characters.get(l_letter, 0) + 1

char_list = sorted( [ ( j , i ) for ( i , j ) in characters.items()], reverse=True)
total = 0

for i,j in char_list:
    float(i)
    total += i
    
for i,j in char_list:
    print(i,j, round(i/total*100,2),"%")
