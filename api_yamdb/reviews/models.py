from django.db import models
from reviews.validators import validete_year
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Категория',
        help_text='Введите название категории.'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
        help_text='Введите slug категории.'
    )

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Жанр',
        help_text='Введите название жанра.'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug',
        help_text='Введите slug жанра.'
    )

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название произведения',
        help_text='Введите название произведения.'
    )
    year = models.PositiveSmallIntegerField(
        db_index=True,
        validators=[validete_year],
        verbose_name='Год выхода произведения',
        help_text='Введите годы выхода произведения.'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        help_text='Выберите категорию.'
    )
    description = models.TextField(
        default='',
        verbose_name='Описание произведения',
        help_text='Введите описание произведения.'
    )
    genre = models.ManyToManyField(
        Genre,
        default=None,
        null=True,
        blank=True
        verbose_name='Жанр',
        help_text='Выберите жанр.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления произведения в каталог.'
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
        help_text='Произведение к которому относится отзыв.'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст отзыва.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
        help_text='Автор отзыва.'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        help_text='Оценка от 1 до 10).'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Дата когда был опубликован отзыв.'
    )

    class Meta:
        ordering = ('-pub_date', )
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            ),
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Дата публикации',
        help_text='Произведение к которому относится коментарий.'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
        help_text='Отзыв к которому относится коментарий.'
    )
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст коментария.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор коментария.'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Дата когда опубликован коментарий.'
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Коментарий'
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.text[:15]
