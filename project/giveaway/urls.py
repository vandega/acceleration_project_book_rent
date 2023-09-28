from django.urls import path
from . import views


urlpatterns = [
    # Book view endpoints
    path('book/list', views.BookListAPIView.as_view(), name='book_list'),
    path('book/new/', views.BookCreateAPIView.as_view(), name='book_create'),
    path('book/delete/<int:pk>/', views.BookDeleteAPIView.as_view(), name="book_delete"),
    path('book/edit/<int:pk>/', views.BookEditAPIView.as_view(), name='book_edit'),

    # Author view endpoints
    path('author/add/', views.AuthorCreateAPIView.as_view(), name='author_create'),
    path('author/list/', views.AuthorListAPIView.as_view(), name='author_list'),
    path('author/delete/<int:pk>/', views.AuthorDeleteAPIView.as_view(), name='author_delete'),
    path('author/edit/<int:pk>/', views.AuthorEditAPIView().as_view(), name='author_edit'),

    # genre view endpoint
    path('genre/list/', views.GenreListAPIView.as_view(), name='genre_list'),
    path('genre/add/', views.GenreCreateAPIView.as_view(), name='genre_create'),
    path('genre/delete/<int:pk>/', views.GenreDeleteAPIView.as_view(), name='genre_delete'),
    path('genre/edit/<int:pk>/', views.GenreEditAPIView.as_view(), name='genre_edit'),

    # condition view endpoints
    path('condition/list/', views.ConditionCreateAPIView.as_view(), name='condition_list'),
    path('condition/admintools/<int:pk>/', views.ConditionDetailsAPIView.as_view(), name='condition_control_for_admin_DELETE'),

]

