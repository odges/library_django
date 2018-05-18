from django.contrib import admin
from .models import Author, Genre, book, BookInstance

# Register your models here.
admin.site.register(Genre)

#admin.site.register(book)
#admin.site.register(BookInstance)

class booksInLine(admin.TabularInline):
	model = book
	extra = 0
	
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name', 'date_birth', 'date_death')
	fields = ['first_name', 'last_name', ('date_birth', 'date_death')]
	inlines = [booksInLine]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

admin.site.register(book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
	list_display =('book', 'id', 'status', 'due_back')
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
			'fields': ('book','id')
		}),
		('Availability', {
			'fields': ('status', 'due_back')
		}),
	)
admin.site.register(BookInstance, BookInstanceAdmin)

