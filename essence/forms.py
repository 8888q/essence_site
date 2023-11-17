from django import forms
from essence.models import YoutubeQuote, TextQuote

class QuoteForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)

class YoutubeQuoteForm(QuoteForm):
    youtube_link = forms.CharField(max_length=200)
    class Meta:
        model = YoutubeQuote
        fields = ["start_seconds", "end_seconds"]

class TextQuoteForm(QuoteForm):
    class Meta:
        model = TextQuote
        fields = ["quote_text", "author", "text_title"]