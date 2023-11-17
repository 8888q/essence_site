from django.urls import path

from . import views

app_name = "essence"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("newyt/", views.YoutubeQuoteCreateView.as_view(), name="youtube_create"),
    path("newtext/", views.TextQuoteCreateView.as_view(), name="text_create"),
    path("youtubequote/<int:pk>/", views.YoutubeQuoteView.as_view(), name="youtube_detail"),
    path("textquote/<int:pk>/", views.TextQuoteView.as_view(), name="text_detail"),
]