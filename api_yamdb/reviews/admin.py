from django.contrib import admin
from reviews.models import Category, Genre, Title, Review, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category',
                    'description', 'pub_date',)
    search_fields = ('name', 'year', 'pub_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author',
                    'score', 'pub_date')
    search_fields = ('title', 'score', 'pub_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'review', 'text', 'author',
                    'pub_date',)
    search_fields = ('review', 'pub_date',)
