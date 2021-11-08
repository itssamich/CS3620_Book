from django.db import models

# Create your models here.
class BookData(models.Model):
    def __str__(self):
        return self.bookTitle
    
    bookTitle = models.CharField(max_length=200, default = '')
    bookAuthor = models.CharField(max_length=200, default = '')
    bookCategory = models.CharField(max_length=200, default = '')
    bookDescription = models.CharField(max_length=2000, default = '')
    bookRating = models.FloatField(default=0)
    bookImage = models.ImageField(upload_to='images', default = 'images/none/noimg.jpg')