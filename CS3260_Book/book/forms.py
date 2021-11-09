from django import forms
from .models import BookData

class bookForm(forms.ModelForm):
    class Meta:
        model = BookData
        fields = ['bookTitle', 'bookAuthor', 'bookCategory', 'bookDescription', 'bookRating', 'bookImage']
        labels = {
            'bookTitle': 'Title',
            'bookAuthor': 'Author',
            'bookCategory': 'Genre(s)',
            'bookDescription': 'Description',
            'bookRating': 'Rating(?/5)',
            'bookImage': 'Cover Art',
        }