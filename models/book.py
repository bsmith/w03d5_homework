class Book:
    def __init__(self, title: str, author: str, genre: str, checked_out: bool = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out