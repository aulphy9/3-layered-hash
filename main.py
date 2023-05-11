"""
Main file to drive 3 layered hash class, and take user input
to perform specified actions.
(Note, this was run and compiled on Python 3.11, which is the latest version of python,
also, for the input file to work correctly, the python open function needs the full file path,
so make sure to modify that to your own system when downloading the zip file and running)
"""
import string
import math
import time
from hash import hashTable

#hash table testing
input_file = open("C:\cp312\layered_hash\input.txt", "r") #filepath will change depending on where you compile
lines = input_file.readlines()
table = hashTable(26)

for line in lines: #inserting lines into hashtable from input file (750 words)
    word = line[0:3] #getting word
    defn = line[4:len(line)-1] #getting defintion
    table.insert(word, defn) #inserting into table

input_file.close()

#block of program to connect user and hashtable
table.options()

option = int(input("Enter your option here: "))

while (option != 4): #looping until user decides to end the program
    if (option == 1): #search table
        word = str(input("Enter a 3 letter word in all caps to search in the table: "))
        if (len(word) == 3):
            found, defn = table.search(word)
            if (found == 1): #found the word
                print(word, defn)
            else:
                print("Word not found")
        else:
            print("Invalid word length")
    elif (option == 2): #insert into table
        word = str(input("Enter a 3 letter word in all caps to insert into the table: "))
        defin = str(input("Enter the definition of the word you entered above: "))
        if (len(word) == 3):
            found, defn = table.search(word)
            if (found == 0): #word not found in table already, continue with insert
                table.insert(word, defin)
                print("Word inserted successfully")
            else:
                print("Word already in hash table")
        else:
            print("Invalid word length")      

    elif (option == 3): #delete from table
        word = str(input("Enter the word you would like to delete from the table: "))
        if (len(word) == 3): #valid letter length
            found, defin = table.search(word)
            if (found == 1): #word exists in table
                table.delete(word)
                print("Word deleted successfully")
            else:
                print("Word does not exist in table")
        else:
            print("Invalid word length")

    time.sleep(2)
    print("")
    table.options()
    option = int(input("Enter your option here: "))
    