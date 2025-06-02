from django.db import transaction, IntegrityError
from .models import Author, Publisher, Book, Store

@transaction.atomic
def create_book_entry():
    try:
        with transaction.atomic():
            publisher = Publisher.objects.create(name = 'Penguin Randome house')

            book = Book.objects.create(
                name = 'The django journey',
                pages = 3000,
                price = 500,
                rating = 4.5,
                publisher=publisher,
                pubdate='2025-05-29'
            )

            authors_data = [
                {'name' : 'Alice', 'age':24},
                {'name' : 'smith', 'age':20},
            ]

            for author_info in authors_data:
                author = Author.objects.create(
                    name=author_info['name'],
                    default={'age':author_info['age']}
                )  
                book.authors.add(author)    

            store = Store.objects.create(name='Downtown BookStore')
            store.books.add(book)

            return book
    except IntegrityError:
        print("Opps ! Data Integrity violated, transaction rolled back")

