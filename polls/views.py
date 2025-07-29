from django.utils import timezone
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Question, Choice, Book, Author
from .form import BookForm
from .services import create_book_entry
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class QuestionListView(generic.ListView):
    model = Question
    template_name = "polls/question_list.html"

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class BookListView(generic.ListView):
    model = Book
    template_name = "polls/book_list.html"
    context_object_name = "books"


class BookPageView(generic.ListView):
    model = Book
    template_name = "polls/book_page.html"
    context_object_name = "page_obj"
    paginate_by = 5


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "polls/book_form.html"
    success_url = reverse_lazy("polls:book_list")


class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "polls/book_form.html"
    success_url = reverse_lazy("polls:book_list")


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "polls/book_confirm_delete.html"
    success_url = reverse_lazy("polls:book_list")


class AuthorListView(generic.ListView):
    model = Author
    template_name = "polls/author_list.html"
    context_object_name = "authors"


class AddBookServiceView(generic.View):
    def get(self, request):
        try:
            book = create_book_entry()
            return HttpResponse(f"Book '{book.name}' created successfully.")
        except Exception as e:
            return HttpResponse(f"Error occurred: {str(e)}")


class VoteView(generic.View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            return render(request, "polls/detail.html", {
                "question": question,
                "error_message": "You didn't select a choice.",
            })
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            return HttpResponseRedirect(reverse_lazy("polls:results", args=(question.id,)))
