from typing import Any
from django import forms
from essence.models import YoutubeQuote, TextQuote
from essence.youtubeapi import video_id, video_info
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


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

    def clean(self):
        youtube_id = self.cleaned_data["youtube_link"]
        start_seconds = self.cleaned_data["start_seconds"]
        end_seconds = self.cleaned_data["end_seconds"]

        length = video_info(video_id(youtube_id))["length"]
        if start_seconds >= end_seconds:
            self.add_error("start_seconds", "Start seconds must be less than End seconds")
            self.add_error("end_seconds", "End seconds must be greater than Start seconds")
        if start_seconds >= length:
            self.add_error("start_seconds", "Start seconds must be less than video length")
        if end_seconds > length:
            self.add_error("end_seconds", "End seconds cannot be greater than video length")

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