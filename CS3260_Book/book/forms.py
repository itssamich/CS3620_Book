from django import forms
from .models import BookData

class bookForm(forms.ModelForm):
    class Meta:
        model = BookData
        fields = ['bookTitle', 'bookAuthor', 'bookCategory', 'bookDescription', 'bookRating', 'bookImage']
        labels = [
            'Title: ',
            'Author: ',
            'Genre(s): ',
            'Description: ',
            'Rating(?/5): ',
            'Cover Art: ',
        ]