# Book.py
from Media import Media

class Book(Media):
    def __init__(self, bookID, title, average_rating, authors, isbn, isbn13, 
                 language_code, num_pages, ratings_count, publication_date, 
                 publisher):
        # Columns from data
        # - bookID: Book ID
        # - title: Book title
        # - authors: Book authors
        # - average_rating: Average rating of the book
        # - isbn: ISBN number
        # - isbn13: ISBN-13 number
        # - language_code: Language code of the book
        # - num_pages: Number of pages in the book
        # - ratings_count: Number of ratings for the book
        # - publication_date: Publication date of the book
        # - publisher: Publisher of the book

        super().__init__(bookID, title, average_rating)
        self.authors = authors
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.publication_date = publication_date
        self.publisher = publisher

    # Accessor methods
    def get_authors(self):
        return self.authors

    def get_isbn(self):
        return self.isbn

    def get_isbn13(self):
        return self.isbn13

    def get_language_code(self):
        return self.language_code

    def get_num_pages(self):
        return self.num_pages

    def get_ratings_count(self):
        return self.ratings_count

    def get_publication_date(self):
        return self.publication_date

    def get_publisher(self):
        return self.publisher

    # Mutator methods
    def set_authors(self, authors):
        self.authors = authors

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_isbn13(self, isbn13):
        self.isbn13 = isbn13

    def set_language_code(self, language_code):
        self.language_code = language_code

    def set_num_pages(self, num_pages):
        self.num_pages = num_pages

    def set_ratings_count(self, ratings_count):
        self.ratings_count = ratings_count

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    def set_publisher(self, publisher):
        self.publisher = publisher