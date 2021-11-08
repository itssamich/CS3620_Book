from django.shortcuts import render
from .models import BookData
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

def addBook(request):
    return render(request, 'Book/addBook.html', {})