from django.utils import timezone
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from .services import create_book_entry
from django.core.paginator import Paginator
from .models import Choice, Question, Book

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls.index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]   


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You did't select a choice"
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

def book_page(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/book_page.html', {'page_obj': page_obj})

def author_list(request):
    authors = Author.objects.all()
    return render(request, "polls/author_list.html", {"authors" : authors})


def add_book_view(request):
    try:
        book = create_book_entry()
        return HttpResponse(f"Book '{book.name}' create successfuly")
    except Exception as e:
        return HttpResponse(f"Error occurred : {str(e)}")    

def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {"form" : form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance = book)
    return render(request, 'books/book_form.html',{"form" : form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book':book})