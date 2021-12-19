from django.urls import path
from . import views

app_name = "shopApp"

urlpatterns = [
    # path('', views.index, name='index'), # for Function
    # path('', views.Index.as_view(), name='index'), # for class
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product"),
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart, name='remove-from-cart'),
]

# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('product/<int:pk>', ProductView.as_view(), name="product"),
#     path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
#     path('remove-from-cart/<int:pk>', remove_from_cart, name='remove-from-cart'),
# ]

# urlpatterns = [
#     # path('', views.index, name='index'), # for Function
#     path('', views.Index.as_view(), name='index'), # for template
#     path('books/', views.BookListView.as_view(), name='books'),
#     path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
#     path('authors/', views.AuthorListView.as_view(), name='authors'),
#     path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
#
#     path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#
#     path('book/<slug:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
#
#     path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
#     path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
#     path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
# ]
