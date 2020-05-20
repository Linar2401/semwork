import datetime

# Create your models here.
import django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone

from semestrovka.settings import BOOK_CATALOGE_NAME
from utils.models import CustomUser


class Label(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Genre(Label):
    pass


class Warning(Label):
    pass


class Rating(Label):
    pass


class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Автор")
    genres = models.ManyToManyField(Genre, blank=True, verbose_name="Жанры")
    warnings = models.ManyToManyField(Warning, blank=True, verbose_name="Предупреждения")
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING, null=True, blank=True,
                               verbose_name="Возрастной рейтинг")
    user_score = models.DecimalField(verbose_name="Оценка", max_digits=2, decimal_places=1, default=0)
    request = models.ForeignKey('BookRequest', on_delete=models.DO_NOTHING, blank=True, null=True)

    pub_date = models.DateField(verbose_name="Дата публикации", default=timezone.now)

    def book_path(self, filename):
        return 'users/{0}/{1}/{2}/{3}'.format(self.user.id, BOOK_CATALOGE_NAME, self.name, filename)

    image = models.ImageField(upload_to=book_path, null=True, blank=True)
    file_fb2 = models.FileField(upload_to=book_path, null=True, blank=True)
    file_txt = models.FileField(upload_to=book_path, null=True, blank=True)
    file_epub = models.FileField(upload_to=book_path, null=True, blank=True)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('books:view', args=[self.id])


class Review(models.Model):
    A = 0.5
    B = 1.0
    C = 1.5
    D = 2.0
    E = 2.5
    F = 3.0
    G = 3.5
    H = 4.0
    I = 4.5
    J = 5.0
    MARK_CHOICES = (
        (A, '0.5'),
        (B, '1.0'),
        (C, '1.5'),
        (D, '2.0'),
        (E, '2.5'),
        (F, '3.0'),
        (G, '3.5'),
        (H, '4.0'),
        (I, '4.5'),
        (J, '5.0'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Автор")
    text = models.TextField(null=True)
    mark = models.DecimalField(verbose_name="Оценка", max_digits=2, decimal_places=1, default=5.0, max_length=2,
                               choices=MARK_CHOICES)

    def __str__(self):
        return "Рецензия" + self.book.name

    def get_absolute_url(self):
        return reverse_lazy('books:review_view', args=[self.id])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга", blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Автор")
    text = models.CharField(max_length=500, blank=True)
    pub_date = models.DateTimeField(verbose_name="Дата комментирования", default=datetime.datetime.now())

    def __str__(self):
        return self.user.username + ' | ' + self.book.__str__()

    def get_absolute_url(self):
        return reverse_lazy('books:review_view', args=[self.book.id])


class BookRequest(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Автор")
    genres = models.ManyToManyField(Genre, blank=True, verbose_name="Жанры")
    warnings = models.ManyToManyField(Warning, blank=True, verbose_name="Предупреждения")
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING,
                               verbose_name="Возрастной рейтинг", null=True)
    text = models.TextField(max_length=1500, blank=True, verbose_name="Текст заявки")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('books:request_view', args=[self.id])


class BookCollection(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Автор")
    open = models.BooleanField(default=False)
    books = models.ManyToManyField(Book, blank=True, verbose_name="Книги")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('books:collection_view', args=[self.id])
