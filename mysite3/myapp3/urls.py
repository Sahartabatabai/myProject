from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('success/', views.success, name='success'),              
   path('books/', views.book_list, name='book_list'),
   path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
   path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
   path('book_list/', views.book_list, name='book_list'),
   path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
   path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
   path('book-list/', views.book_list, name='book_list'),
   path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
   path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]   

