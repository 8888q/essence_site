from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .models import Quote, TextQuote, YoutubeQuote, YoutubeVideo
from .forms import YoutubeQuoteForm, TextQuoteForm
from .youtubeapi import video_id, video_info

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "essence/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["youtube"] = YoutubeQuote.objects.all()
        context["text"] = TextQuote.objects.all()
        return context
    
class TextQuoteIndexView(generic.ListView):
    template_name = "essence/list.html"
    context_object_name = "quotes"

    def get_queryset(self) -> QuerySet[Any]:
        return TextQuote.objects.all().order_by("-metadata__entry_timestamp")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["text"] = True
        return context
    

class YoutubeQuoteIndexView(generic.ListView):
    template_name = "essence/list.html"
    context_object_name = "quotes"

    def get_queryset(self) -> QuerySet[Any]:
        return YoutubeQuote.objects.all().order_by("-metadata__entry_timestamp")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["youtube"] = True
        return context
    
class YoutubeQuoteCreateView(generic.CreateView):
    template_name = "essence/create.html"
    model = YoutubeQuote
    form_class = YoutubeQuoteForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ytquote = form.save(commit=False)
        youtube_id = video_id(form.cleaned_data['youtube_link'])
        query = YoutubeVideo.objects.filter(pk=youtube_id)
        # if we don't have the yt video yet, store it
        if len(query) == 0:
            info = video_info(youtube_id)
            youtube_video = YoutubeVideo(id = youtube_id, channel=info['channel'], title=info['title'], length=info['length'])
            youtube_video.save()
        else:
            youtube_video = query.get()
        ytquote.youtube_id = youtube_video
        quote = Quote(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
        quote.save()
        ytquote.metadata = quote
        ytquote.save()
        
        self.success_url = reverse("essence:youtube_detail", args=(ytquote.pk,))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["youtube"] = True
        return context
    

class YoutubeQuoteView(generic.DetailView):
    model = YoutubeQuote
    template_name = "essence/youtubedetail.html"
    

class TextQuoteCreateView(generic.CreateView):
    template_name = "essence/create.html"
    model = TextQuote
    form_class = TextQuoteForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        text_quote = form.save(commit=False)
        quote = Quote(title=form.cleaned_data['title'], description=form.cleaned_data['description'])
        quote.save()
        text_quote.metadata = quote
        text_quote.save()
        
        self.success_url = reverse("essence:text_detail", args=(text_quote.pk,))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = True
        return context
    

class TextQuoteView(generic.DetailView):
    model = TextQuote
    template_name = "essence/textdetail.html"