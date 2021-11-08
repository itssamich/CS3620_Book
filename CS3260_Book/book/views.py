from django.shortcuts import render
from .models import BookData

# Create your views here.
def bookList(request):
    bookObject = BookData.objects.all()
    return render(request, 'Book/bookList.html', {'bookObject': bookObject})