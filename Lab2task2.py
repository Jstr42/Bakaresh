class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки с необязательным списком книг.
        Если книги не переданы, создаётся пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает идентификатор для добавления новой книги.
        Если книг нет, возвращает 1. Иначе возвращает последний id + 1.
        """
        return 1 if not self.books else max(self.books, key=lambda book: book.id).id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги с заданным id в списке книг.
        Если книга не найдена, вызывает ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "test_name_1",
            "pages": 200,
        },
        {
            "id": 2,
            "name": "test_name_2",
            "pages": 400,
        }
    ]

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))