from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration.as_view(), name='user'),
    path('<int:pk>/', views.DeleteUser.as_view(), name='delate_or_show'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('list/', views.user_list, name='users_list')
]