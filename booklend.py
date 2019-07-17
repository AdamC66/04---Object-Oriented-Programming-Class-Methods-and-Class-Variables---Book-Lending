import random
from datetime import datetime

class Book:
    on_shelf = []
    on_loan = []
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def borrow(self):
        if not (self.lent_out()):
            Book.on_loan.append(self)
            Book.on_shelf.remove(self)
            self.due_date = self.current_due_date()
            return True
        else:
            return False
    def return_to_library(self):
        if (self.lent_out()):
            Book.on_loan.remove(self)
            Book.on_shelf.append(self)
            self.due_date = None
            return True
        else:
            return False
    
    def lent_out(self):
        return (self in Book.on_loan)

    @classmethod
    def create(cls, title, author, isbn):
        newbook = Book(title, author, isbn)
        cls.on_shelf.append(newbook)
        return(newbook)
    
    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue(cls):
        overdue_books = []
        for book in cls.on_loan:
            if book.due_date < datetime.now():
                cls.overdue_books.append(book.title)
        return overdue_books
    @classmethod
    def browse(cls):
        return(random.choice(cls.on_shelf))

sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")
print(Book.browse().title) # Random Book Title
print(Book.browse().title) # Random Book Title
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