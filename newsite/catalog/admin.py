from django.contrib import admin
from .models import Author, Genre, book, BookInstance

# Register your models here.

admin.site.register(Genre)

#admin.site.register(book)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name', 'date_birth', 'date_death')

admin.site.register(Author, AuthorAdmin)



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

admin.site.register(book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
admin.site.register(BookInstance, BookInstanceAdmin)