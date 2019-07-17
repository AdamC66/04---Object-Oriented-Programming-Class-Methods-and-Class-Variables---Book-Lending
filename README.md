# 04---Object-Oriented-Programming-Class-Methods-and-Class-Variables---Book-Lending

Before starting this assignment you should have some familiarity with
lists and iteration
if/else statements
defining classes and instantiating objects
defining and calling instance methods
using instance variables
You should also have already completed the previous assignments on class methods and class variables.

Learning Goals
class variables
class methods
Part 3: Book Lending
In this assignment you're going to build a book lending program in order to practice using class variables and class methods. We'll be using a few of Python's built-in modules to help us: datetime and random.

More on random
random is the Python module that allows us to incorporate randomness into our programs. In the previous exercise, we used the randint() function from this module to generate random numbers. In this next exercise, we'll be using the choice() function to help us pick a random element from a list.

Remember, random isn't loaded by default when you start a Python program/the Python shell, so we have to tell Python so load it using import:

import random
Try defining a list and passing it in to random.choice() a few times to see how this function works:

>>>options = [15,20,34923,31,3,5,86,1]
>>> random.choice(options) # pick a random item from the list of options
>>> random.choice(options) # and again
>>> random.choice(options) # and again
Working with datetime
In this exercise we're going to import a second Python module: datetime. The datetime module helps us work with date and time data. Specifically, we're going to use it to manage the due dates of the books in our library. Before getting started on the book program, open the Python shell and the datetime docs and spend a few minutes familiarizing yourself with this part of Python:

Just like with random, we have to tell Python to load datetime using an import statement:

>>> from datetime import datetime
>>> now = datetime.now()
>>> now
# datetime.datetime(2018, 12, 14, 17, 7, 5, 190626) <--- the current date and time
>>> now.timestamp()
# 1544825225.190626 <--- the current date and time represented as the number of seconds that have passed since January 1st 1970 at midnight UTC time (that's when they started counting!)
>>> one_hour = 60 * 60 # 60 seconds times 60 minutes
>>> now.timestamp() + one_hour
# 1544828825.190626 <---- an hour from now (as a "timestamp")
>>> hour_from_now = now.timestamp() + one_hour
>>> datetime.fromtimestamp(hour_from_now)
# datetime.datetime(2018, 12, 14, 18, 7, 5, 190626) <--- an hour from now (as a datetime obj)
Why are we saying "datetime" twice in the statement from datetime import datetime? Previously, we were importing specific functions: from random import randint imports the randint function from the random module. Here, instead of importing a function, we're importing a new data type, called datetime.

type(datetime)
# <class 'type'>
Your task
Create a class called Book.
Add from datetime import datetime at the top of the file, so we can work with datetimes to set due dates on borrowed books.
Your class should have two class variables: on_shelf and on_loan. Both should start as empty lists. on_shelf will contain the collection of book objects that are available to be lent out and on_loan will contain the collection of books that are currently being borrowed.
Your class should have the following methods:
an instance method __init__
an instance method borrow
an instance method return_to_library
an instance method lent_out
a class method create
a class method current_due_date
a class method overdue_books
a class method browse
__init__
This instance method makes a new book object. It should initialize a book's title, author, and ISBN.

create
This class method is how new books are added to the library. This method should make a new book object with Book(...),add the new book object to on_shelf, and then return the new book.

browse
This class method should return a random book from on_shelf (remember random.choice()?).

lent_out
This instance method should return true if a book has already been borrowed and false otherwise.

current_due_date
This class method returns the due date for books taken out today. We've written the body of this one for you:

    now = datetime.now()
    two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
    future_timestamp = now.timestamp() + two_weeks
    return datetime.fromtimestamp(future_timestamp)
borrow
This instance method is how a book is taken out of the library. This method should use lent_out to check if the book is already on loan, and if it is this method should return False to indicate that the attempt to borrow the book failed. Otherwise, use current_due_date to set the due_date of the book and move it from the collection of available books to the collection of books on loan, then return True.

return_to_library
This instance method is how a book gets returned to the library. It should call lent_out to verify that the book was actually on loan. If it wasn't on loan in the first place, return False. Otherwise, move the book from the collection of books on loan to the collection of books on the library shelves, and set the book's due date to None before returning True.

overdue
This class method should return a list of books whose due dates are in the past (ie. less than Time.now).

As you write your program you should be thinking about the reasoning behind making each method either an instance method or a class method.

Example output
sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # "Sister Outsider" (this value may be different for you)
print(Book.browse().title) # "Ain't I a Woman?" (this value may be different for you)
print(len(Book.on_shelf)) # 3
print(len(Book.on_loan)) # 0
print(sister_outsider.lent_out()) # False
print(sister_outsider.borrow()) # True
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 1
print(sister_outsider.lent_out()) # True
print(sister_outsider.borrow()) # False
print(sister_outsider.due_date) # 2017-02-25 20:52:20 -0500 (this value will be different for you)
print(len(Book.overdue())) # 0
print(sister_outsider.return_to_library()) # True
print(sister_outsider.lent_out()) # False
print(len(Book.on_shelf)) # 2
print(len(Book.on_loan)) # 0
Stretch goals
Add a renew method to push the due date back.
If someone tries to borrow a book and it's already on loan, find a way to indicate that the book has been put on hold. If a book is on hold you shouldn't be able to renew it.
Add a genre to each book and allow users to browse by genre.
Add a class method that accepts a title, author, or isbn as an argument and returns all books that match.
