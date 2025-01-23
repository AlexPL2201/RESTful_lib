from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Создание тестовых данных
        self.book1 = Book.objects.create(
            header='Грокаем алгоритмы (2-ое издание)',
            author='А. Бхаргава',
            publication_year='2024-09-23',
            genre='Научная литература'
        )

        self.book2 = Book.objects.create(
            header='Грокаем машинное обучение',
            author='Л. Серрано',
            publication_year='2024-01-01',
            genre='Научная литература'
        )

    def test_get_books(self):
        """Тест получения списка всех книг"""
        url = reverse('book-list-create')
        response = self.client.get(url)
        books = Book.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), books.count())

    def test_create_books(self):
        """Тест создания новой книги"""
        url = reverse('book-list-create')
        data = {
            'header': 'Паттерны разработки на Python',
            'author': 'Г. Персиваль, Б. Грегори',
            'publication_year': '2022-01-01',
            'genre': 'Научная литература'
        }
        books_count_before_adding = Book.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), books_count_before_adding + 1)

    def test_get_book_detail(self):
        """Тест получения детальной информации о книге по ID"""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['header'], self.book1.header)

    def test_delete_book(self):
        """Тест удаления книги"""
        url = reverse('book-detail', args=[self.book1.id])
        books_count_before_deleting = Book.objects.count()
        respoonse = self.client.delete(url)
        self.assertEqual(respoonse.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), books_count_before_deleting - 1)

    def test_update_book(self):
        """Тест обновления информации о книге"""
        url = reverse('book-detail', args=[self.book2.id])
        data = {
            'header': 'Грокаем машинное обучение (Обновлено)',
            'author': 'Л. Серрано',
            'publication_year': '2024-01-02',
            'genre': 'Научная литература'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.header, data['header'])