class Book:
    def __init__(self, title: str, author: str, genre: str, checked_out: bool = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.accession_id = None
    
    def check_in(self):
        self.checked_out = False
    
    def check_out(self):
        self.checked_out = True

    def get_accession_id(self):
        return self.accession_id

    def update_accession_id(self, accession_id: int):
        self.accession_id = accession_id
    
    def remove_accession_id(self):
        self.accession_id = None