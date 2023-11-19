from django import forms
from essence.models import YoutubeQuote, TextQuote

class QuoteForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder' :'Description', 'class': 'form-control', 'style': 'height: 8ch'}))

class YoutubeQuoteForm(QuoteForm):
    youtube_link = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Youtube Link', 'class': 'form-control'}))
    class Meta:
        model = YoutubeQuote
        fields = ["start_seconds", "end_seconds"]
        widgets = {
            'start_seconds': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 16ch;',
                'placeholder': 'Start seconds'
                }),
            'end_seconds': forms.NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 16ch;',
                'placeholder': 'End seconds'
                })
        }

    field_order = ["title", "description", "youtube_link", "start_seconds", "end_seconds"]

class TextQuoteForm(QuoteForm):
    class Meta:
        model = TextQuote
        fields = ["quote_text", "author", "text_title"]
        widgets = {
            'author': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Author'
                }),
            'text_title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Title of Work'
                }),
            'quote_text': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Quote Text'
                })
        }

    field_order = ["title", "description", "quote_text", "text_title", "author"]