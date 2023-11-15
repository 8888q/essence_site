from django.db import models
from django.utils import timezone


# Create your models here.
class BookQuote(models.Model):
    quote_text = models.TextField()
    book_name = models.CharField(max_length=200)
    entry_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '\"' + self.quote_text + '\", ' + self.book_name