from django.urls import path
from .views import book_page, book_list

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    path("<int:question_id>/vote/", views.vote, name="vote"),

    path('books/', book_page, name='book_page'),

    path('author/', views.author_list, name='author_list'),
    path('', views.index, name="index"),
    path('books/', views.book_list, name="book_list"),
    path('books/add/', views.book_create, name="book_create"),
    path('books/<int:pk>/edit/', views.book_update, name="book_update"),
    path('books/<int:pk>/delete/', views.book_delete, name="book_delete"),
]
