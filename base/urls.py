from django.urls import path
from base import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('articles/', views.ArticlesView.as_view()),
    path('articles/<int:pk>', views.ArticleDetailView.as_view()),
    path('authors/', views.AuthorsView.as_view()),
    path('authors/<int:pk>', views.AuthorDetailView.as_view()),
    path('users/', views.UsersView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
]
