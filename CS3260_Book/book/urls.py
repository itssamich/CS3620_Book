from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book'

urlpatterns = [
    path('', views.bookList, name='bookList'),
    path('addBook', views.addBook, name='addBook'),
    path('<int:bookId>', views.detail, name='detail'),
]