from django.core.management.base import BaseCommand
from book.models import Book


class Command(BaseCommand):
    help = "Create 10 predefined books"

    def handle(self, *args, **kwargs):
        books = [
            {
                "isbn": "9780140449136",
                "title": "The Odyssey",
                "author": "Homer",
                "genre": "Epic",
                "published_date": "1996-11-01",
                "total_copies": 10,
                "available_copies": 10,
            },
            {
                "isbn": "9780439139601",
                "title": "Harry Potter and the Goblet of Fire",
                "author": "J.K. Rowling",
                "genre": "Fantasy",
                "published_date": "2000-07-08",
                "total_copies": 15,
                "available_copies": 15,
            },
            {
                "isbn": "9780061120084",
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "genre": "Fiction",
                "published_date": "1960-07-11",
                "total_copies": 12,
                "available_copies": 12,
            },
            {
                "isbn": "9780553213119",
                "title": "Dracula",
                "author": "Bram Stoker",
                "genre": "Horror",
                "published_date": "1897-05-26",
                "total_copies": 8,
                "available_copies": 8,
            },
            {
                "isbn": "9781501173219",
                "title": "It Ends With Us",
                "author": "Colleen Hoover",
                "genre": "Romance",
                "published_date": "2016-08-02",
                "total_copies": 20,
                "available_copies": 20,
            },
            {
                "isbn": "9780451524935",
                "title": "1984",
                "author": "George Orwell",
                "genre": "Dystopian",
                "published_date": "1949-06-08",
                "total_copies": 14,
                "available_copies": 14,
            },
            {
                "isbn": "9780141439600",
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "genre": "Romance",
                "published_date": "1813-01-28",
                "total_copies": 9,
                "available_copies": 9,
            },
            {
                "isbn": "9780544003415",
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "genre": "Fantasy",
                "published_date": "1937-09-21",
                "total_copies": 13,
                "available_copies": 13,
            },
            {
                "isbn": "9780141182803",
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "genre": "Tragedy",
                "published_date": "1925-04-10",
                "total_copies": 11,
                "available_copies": 11,
            },
            {
                "isbn": "9780385472579",
                "title": "Zen and the Art of Motorcycle Maintenance",
                "author": "Robert M. Pirsig",
                "genre": "Philosophical fiction",
                "published_date": "1974-04-01",
                "total_copies": 10,
                "available_copies": 10,
            },
        ]

        for book in books:
            Book.objects.create(**book)

        self.stdout.write(self.style.SUCCESS("Successfully created 10 book entries."))
