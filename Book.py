class Book:
    def __init__(self, title, author,ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.available=True

    @property
    def is_available(self):
        return self.currrnt_loan is None    

    def __str__(self):
        return(f"Title: {self.title}",
               f"Author: {self.author}",
               f"ISBN: {self.ISBN}",
               f"Is available: {'Yes' if self.is_available else 'No'}")    

    def __eq__(self, value):
         if self.ISBN==value:
             return(f"The Books are the same ")
