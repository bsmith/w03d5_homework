class Book:
    def __init__(self, title: str, author: str, genre: str, checked_out: bool = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
    
    def check_in(self):
        self.checked_out = False
    
    def check_out(self):
        self.checked_out = True