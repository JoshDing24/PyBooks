import time 

#This is a clean list to display to the users
bookList = ["The Pudding And The Pastry", "The Sons Of Tomorrow", "The Wyvern Mystery", "Dracula", "The Great Gatsby", "Little Woman", "Moby Dick", "My Mother India", "A Tale Of Two Cities", "Ulysses"]
#This is the file location of the books
bookDirs = ["ThePuddingAndThePastry.txt", "TheSonsOfTomorrow.txt", "TheWyvernMystery.txt", "Dracula.txt", "GreatGatsby.txt", "LittleWoman.txt", "MobyDick.txt", "MyMotherIndia.txt", "TaleOfTwoCities.txt", "Ulysses.txt"]

#This is a function to clear the screen in an attempt to make it more readable and clean
def clear():
    print("\n" * 50)


#This counts the words in book and prints it out. I didnt put it in the other function because that didnt print out the book afterwards
def wordCounter(book):
    clear()
    j = open(bookDirs[book], "r", encoding="utf-8")
    readData = j.read()
    perWord = readData.split()
    print('Total Word count: ', len(perWord))

#This function is used to open the text file and read it
def Reader(book):
    f = open(bookDirs[book], "r", encoding="utf-8")
    #This reads each line in the file one at a time with a delay
    for line in f:
        print(line)
        time.sleep(3)

#Printing the list in a nice way
def bookListFunc():
    for index, book in enumerate(bookList, 1):
        print(f"{index}: {book}")
    print("Or 0 to quit")

#This is the function for asking for their desired book
def userInput():
    clear()
    bookListFunc()
    isValid = 1
    #Making sure we keep asking until the user gives an acceptable input
    while isValid == 1:
        book = ""
        book = input("What book would you like to read? ")
        #Ensuring the book is a numerical value, and if it is turning it into an integer
        if book.isnumeric():
            book = int(book)
            if book == 0:
                quit()
            elif book >= 1 and book <= 10:
                #This is so the user input matches up with the item in the list as a list starts at 0
                book = book - 1
                isValid = 2
                wordCounter(book)
                Reader(book)
                
            else:
                clear()
                print("Error, Please put a valid input")
                bookListFunc()
        else:
            clear()
            print("Error, Please put a valid input")
            bookListFunc()
    return book




#Clearing the screen and running the program
clear()
book = userInput()