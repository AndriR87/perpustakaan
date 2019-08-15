from django.contrib import admin
from katalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)

#define the admin class

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    list_filter = ['date_of_birth', 'first_name']
    search_fields = ['first_name', 'last_name']
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ['title']
    search_fields = ['genre__name__exact', 'title', 'author__first_name']
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

# Register your models here.
