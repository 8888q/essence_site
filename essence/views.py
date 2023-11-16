from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Quote

# Create your views here.
class IndexView(generic.ListView):
    template_name = "essence/index.html"
    context_object_name = "moments"

    def get_queryset(self) -> QuerySet[Any]:
        return Quote.objects.all()