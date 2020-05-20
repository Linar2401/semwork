from django.contrib import admin

# Register your models here.
from books.models import *

# admin.site.register(Genre)
# admin.site.register(Warning)
# admin.site.register(Rating)
admin.site.register(BookRequest)
admin.site.register(BookCollection)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'user_score', 'request', 'pub_date')
    fields = ('user', 'user_score', 'request', 'pub_date', 'name', 'description', ('genres', 'warnings', 'rating'),
              ('image', 'file_fb2', 'file_txt', 'file_epub'),
              'published')
    date_hierarchy = 'pub_date'
    list_display = ('name', 'user', 'pub_date')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'book', 'mark')
    fields = ('user', 'book', 'text', 'mark')
    list_display = ('book', 'user', 'mark')


@admin.register(Comment)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'book', 'pub_date', 'text')
    fields = (('user', 'book'), 'pub_date', 'text')
    list_display = ('book', 'user', 'pub_date')
