from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Brand)
admin.site.register(models.Product)
admin.site.register(models.ProductInstance)
admin.site.register(models.OrderProduct)
admin.site.register(models.Order)
admin.site.register(models.Store)
admin.site.register(models.Supplier)



# class BooksInstanceInline(admin.TabularInline):
#     model = models.BookInstance
#
#
# # admin.site.register(models.Book)
# # Register the Admin classes for Book using the decorator
# @admin.register(models.Book)
# class BookAdmin(admin.ModelAdmin):
#     # list_display = ('title', 'author')
#     list_display = ('title', 'author', 'display_genre')
#     list_filter = ('title', 'author', 'genre')
#     inlines = [BooksInstanceInline]
#
#
# # Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# # Register the admin class with the associated model
# admin.site.register(models.Author, AuthorAdmin)
#
#
# # admin.site.register(models.BookInstance)
# # Register the Admin classes for BookInstance using the decorator
# @admin.register(models.BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }),
#     )
#
# admin.site.register(models.Genre)
