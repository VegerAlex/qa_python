from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest
    from main import BooksCollector

import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert 'Мастер и Маргарита' in collector.get_books_genre()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мертвые души')
        collector.set_book_genre('Мертвые души', 'Классика')
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Классика')
        assert collector.get_books_with_specific_genre('Классика') == ['Мертвые души', 'Преступление и наказание']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        assert collector.get_books_genre() == {'Пикник на обочине': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Сказки Андерсена')
        collector.set_book_genre('Сказки Андерсена', 'Фэнтези')
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.set_book_genre('Гарри Поттер и Философский камень', 'Фэнтези')
        collector.add_new_book('It')
        collector.set_book_genre('It', 'Ужасы')
        assert collector.get_books_for_children() == ['Сказки Андерсена', 'Гарри Поттер и Философский камень']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Фэнтези')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == ['Маленький принц']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Фэнтези')
        collector.add_book_in_favorites('Маленький принц')
        collector.delete_book_from_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Философский камень')
        collector.set_book_genre('Гарри Поттер и Философский камень', 'Фэнтези')
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Фэнтези')
        collector.add_book_in_favorites('Гарри Поттер и Философский камень')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и Философский камень', 'Маленький принц']

    def test_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фэнтези')
        assert collector.get_book_genre('Несуществующая книга') is None



