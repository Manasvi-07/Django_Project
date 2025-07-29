from django.urls import path
from .views import IndexView, DetailView, ResultsView, VoteView, BookListView, BookPageView, BookCreateView, BookDeleteView, BookUpdateView, AuthorListView, AddBookServiceView,QuestionListView

app_name = "polls"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/",DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", VoteView.as_view(), name="vote"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/page/", BookPageView.as_view(), name="book_page"),
    path("books/add/", BookCreateView.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"), 
    path("authors/", AuthorListView.as_view(), name="author_list"),
    path("create-book-service/", AddBookServiceView.as_view(), name="add_book_service"),
    path('questions/', QuestionListView.as_view(), name='question-list'),
]

