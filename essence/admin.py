from django.contrib import admin

# Register your models here.
from .models import Quote, YoutubeQuote, YoutubeVideo, TextQuote

admin.site.register(Quote)
admin.site.register(TextQuote)
admin.site.register(YoutubeVideo)
admin.site.register(YoutubeQuote)