class Library:
    def __init__(self):
        self.collection_of_books=[]
        self.members={}

    def add_books(self, book):
        self.collection_of_books.append(book)  
        print(f"Book {book.title} is added to the Library")     
    