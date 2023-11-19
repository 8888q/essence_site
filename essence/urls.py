from django.urls import path

from . import views

app_name = "essence"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("newyt/", views.YoutubeQuoteCreateView.as_view(), name="youtube_create"),
    path("newtext/", views.TextQuoteCreateView.as_view(), name="text_create"),
    path("textquote/", views.TextQuoteIndexView.as_view(), name="text_index"),
    path("youtubequote/", views.YoutubeQuoteIndexView.as_view(), name="youtube_index"),
    path("textquote/<int:pk>/", views.TextQuoteView.as_view(), name="text_detail"),
    path("youtubequote/<int:pk>/", views.YoutubeQuoteView.as_view(), name="youtube_detail"),
]