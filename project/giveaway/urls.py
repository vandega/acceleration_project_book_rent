from django.urls import path
from . import views


urlpatterns = [
    # Book view endpoints
    path('', views.BookListAPIView.as_view(), name='bookList'),
    path('new/', views.BookCreateAPIView.as_view(), name='newBook'),
    path('delete/<int:pk>/', views.BookDeleteAPIView.as_view(), name="delete_book"),
    path('edit/<int:pk>/', views.BookEditAPIView.as_view(), name='edit_book'),

    # Author view endpoints
    path('add/', views.AuthorCreateAPIView.as_view(), name='add_author'),
    path('list/', views.AuthorListAPIView.as_view(), name='authors'),
    path('delete/<int:pk>/', views.AuthorDeleteAPIView.as_view(), name='delete_Author'),
    path('edit/<int:pk>/', views.AuthorEditAPIView().as_view(), name='edit_author')
]