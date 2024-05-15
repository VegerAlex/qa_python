# qa_python

Описание тестов:

1. `test_add_new_book`: Этот тест проверяет метод `add_new_book()`, который добавляет новую книгу в коллекцию книг. Мы создаем экземпляр класса `BooksCollector`, добавляем новую книгу и затем проверяем, что книга была успешно добавлена, проверяя наличие ее названия в словаре `books_genre`.

2. `test_set_book_genre`: Этот тест проверяет метод `set_book_genre()`, который устанавливает жанр для указанной книги. Мы добавляем новую книгу, затем устанавливаем для нее жанр и проверяем, что жанр был успешно установлен, сравнивая его с ожидаемым значением.

3. `test_get_books_with_specific_genre`: Этот тест проверяет метод `get_books_with_specific_genre()`, который возвращает список книг определенного жанра. Мы добавляем несколько книг с разными жанрами, затем проверяем, что метод возвращает правильный список книг для указанного жанра.

4. `test_get_books_genre`: Этот тест проверяет метод `get_books_genre()`, который возвращает словарь с книгами и их жанрами. Мы добавляем новую книгу с жанром, затем проверяем, что метод возвращает ожидаемый словарь.

5. `test_get_books_for_children`: Этот тест проверяет метод `get_books_for_children()`, который возвращает список книг, подходящих для детей. Мы добавляем несколько книг с разными жанрами и проверяем, что метод возвращает правильный список книг, исключая книги с жанрами, которые не подходят для детей.

6. `test_add_book_in_favorites`: Этот тест проверяет метод `add_book_in_favorites()`, который добавляет книгу в список избранных. Мы добавляем новую книгу в коллекцию, затем добавляем ее в список избранных и проверяем, что она была успешно добавлена.

7. `test_delete_book_from_favorites`: Этот тест проверяет метод `delete_book_from_favorites()`, который удаляет книгу из списка избранных. Мы добавляем новую книгу в список избранных, затем удаляем ее и проверяем, что она была успешно удалена.

8. `test_get_list_of_favorites_books`: Этот тест проверяет метод `get_list_of_favorites_books()`, который возвращает список избранных книг. Мы добавляем несколько книг в список избранных и проверяем, что метод возвращает правильный список избранных книг.

9. `test_set_genre_for_nonexistent_book`: Этот тест проверяет метод `set_book_genre()`, когда пытаемся установить жанр для книги, которая не существует в коллекции. Мы создаем экземпляр класса `BooksCollector`, затем пытаемся установить жанр для книги, которой нет в коллекции, и затем проверяем, что метод `get_book_genre()` возвращает `None` для этой книги.
