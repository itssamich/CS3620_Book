from django.shortcuts import render, redirect
from .models import BookData
from .forms import bookForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def bookList(request):
    bookObject = BookData.objects.all()
    bookName = request.GET.get('bookName')
    if(bookName != '' and bookName is not None):
        bookObject = BookData.objects.filter(bookTitle__icontains=bookName)

    
    paginator = Paginator(bookObject, 10)
    page = request.GET.get('page')
    bookObject = paginator.get_page(page)

    return render(request, 'Book/bookList.html', {'bookObject': bookObject})

def index(request):
    return render(request, 'Book/index.html', {})

def detail(request, bookId):
    book = BookData.objects.get(pk=bookId)
    
    return render(request, 'Book/detail.html', {'book':book})


def addBook(request):
    form = bookForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, 'Book/addBook.html', {'form' :form})