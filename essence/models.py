from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    entry_timestamp = models.DateTimeField(default=timezone.now)
    

class YoutubeVideo(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    channel = models.CharField(max_length=200)
    title = models.TextField()
    length = models.IntegerField()

class TextQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    metadata = models.OneToOneField(Quote, on_delete=models.CASCADE, primary_key=True)
    quote_text = models.TextField()
    author = models.CharField(max_length=200)
    text_title = models.CharField(max_length=200)

    def __str__(self):
        return '\"' + self.quote_text + '\", ' + self.text_title
    

class YoutubeQuote(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    metadata = models.OneToOneField(Quote, on_delete=models.CASCADE)
    youtube_id = models.ForeignKey(YoutubeVideo, on_delete=models.DO_NOTHING)
    start_seconds = models.IntegerField(validators=[validators.MinValueValidator(0)])
    end_seconds = models.IntegerField()

    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(end_seconds__gt=F('start_seconds')), 
                name = 'check_end_seconds',
            ),
        ]