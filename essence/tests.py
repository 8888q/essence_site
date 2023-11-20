from django.test import TestCase
from essence.models import TextQuote, YoutubeQuote, YoutubeVideo, Quote
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import login
from django.test import Client

#to do: add multi-user test cases

class YoutubeQuoteTestCase(TestCase):
    def setUp(self):
        Quote.objects.create(title="Test Title", description="Test Description")
        YoutubeVideo.objects.create(id="nUuhx0q6krU", length=245, title="once in a moon", channel="Sarah Kang Music")
        u = User.objects.create_user(username='testuser', password='12345')
        c = Client()
        c.login(username="testuser", password='12345')
        self.client = c


    def test_youtubequote_start_seconds_gt_0(self):
        """
        Youtube quote start seconds is greater than 0
        """
        ytquote = YoutubeQuote(start_seconds=-1, 
                               end_seconds=1, 
                               user=User.objects.all().get(),
                               metadata=Quote.objects.all().get(), 
                               youtube_id=YoutubeVideo.objects.get(pk="nUuhx0q6krU")
                               )
        self.assertRaises(ValidationError, ytquote.save)

    def test_youtubequote_start_seconds_lt_end_seconds(self):
        """
        Youtube quote start seconds is less than end seconds
        """
        ytquote = YoutubeQuote(start_seconds=2, 
                               end_seconds=1,
                               user=User.objects.all().get(),
                               metadata=Quote.objects.all().get(), 
                               youtube_id=YoutubeVideo.objects.get(pk="nUuhx0q6krU")
                               )
        self.assertRaises(ValidationError, ytquote.save)

    def test_youtubequote_end_seconds_lte_length(self):
        """
        Youtube quote end seconds is less than video length
        """
        ytquote = YoutubeQuote(start_seconds=2, 
                               end_seconds=255,
                               user=User.objects.all().get(),
                               metadata=Quote.objects.get(pk=1), 
                               youtube_id=YoutubeVideo.objects.get(pk="nUuhx0q6krU")
                               )
        self.assertRaises(ValidationError, ytquote.save)

class YoutubeQuoteIndexViewTests(TestCase):
    def setUp(self):
        q = Quote.objects.create(title="Test Title", description="Test Description")
        ytv = YoutubeVideo.objects.create(id="nUuhx0q6krU", length=245, title="once in a moon", channel="Sarah Kang Music")
        u = User.objects.create_user(username='testuser', password='12345')
        c = Client()
        c.login(username="testuser", password='12345')
        self.client = c
        YoutubeQuote.objects.create(user=u, metadata=q, youtube_id=ytv, start_seconds = 1, end_seconds = 5)
        q = Quote.objects.create(title="Test Title1", description="Test Description1")
        ytv = YoutubeVideo.objects.create(id="xMqyhqvJb8I", length=1807, title="Last Bible III -- Underworld Forest", channel="Zangoose")
        YoutubeQuote.objects.create(user=u, metadata=q, youtube_id=ytv, start_seconds = 2, end_seconds = 6)

    def test_index_view_contains_all_quotes(self):
        """
        The index view of youtube quotes contains all youtube quotes
        """
        query = YoutubeQuote.objects.all()
        response = self.client.get(reverse("essence:youtube_index"))
        self.assertQuerySetEqual(
            response.context["quotes"].order_by("pk"),
            query
        )

class TextQuoteIndexViewTests(TestCase):
    def setUp(self):
        User.objects.create(username='Testuser')
        u = User.objects.create_user(username='testuser', password='12345')
        c = Client()
        c.login(username="testuser", password='12345')
        self.client = c
        q = Quote.objects.create(title="Test Title", description="Test Description")
        TextQuote.objects.create(user=u, metadata=q, quote_text="quote text", author="Author", text_title="text title")
        q = Quote.objects.create(title="Test Title1", description="Test Description1")
        TextQuote.objects.create(user=u, metadata=q, quote_text="quote text2", author="Author2", text_title="text title2")

    def test_index_view_contains_all_quotes(self):
        """
        The index view of text quotes contains all text quotes
        """
        query = TextQuote.objects.all()
        response = self.client.get(reverse("essence:text_index"))
        self.assertQuerySetEqual(
            response.context["quotes"].order_by("pk"),
            query
        )

class YoutubeQuoteViewTests(TestCase):
    def setUp(self):
        q = Quote.objects.create(title="Test Title", description="Test Description")
        ytv = YoutubeVideo.objects.create(id="nUuhx0q6krU", length=245, title="once in a moon", channel="Sarah Kang Music")
        u = User.objects.create_user(username='testuser', password='12345')
        c = Client()
        c.login(username="testuser", password='12345')
        self.client = c
        c.login(username='testuser', password='12345')
        self.quote = YoutubeQuote.objects.create(user=u, metadata=q, youtube_id=ytv, start_seconds = 1, end_seconds = 5)

    def test_detail_view_contains_quote_title(self):
        response = self.client.get(reverse("essence:youtube_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.metadata.title)

    def test_detail_view_contains_quote_description(self):
        response = self.client.get(reverse("essence:youtube_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.metadata.description)

    def test_detail_view_contains_correct_youtube_video(self):
        response = self.client.get(reverse("essence:youtube_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.youtube_id.id)

class TextQuoteViewTests(TestCase):
    def setUp(self):
        q = Quote.objects.create(title="Test Title", description="Test Description")
        u = User.objects.create_user(username='testuser', password='12345')
        c = Client()
        c.login(username="testuser", password='12345')
        self.client = c
        self.quote = TextQuote.objects.create(user=u, metadata=q, quote_text="Once upon a time,", author="Author", text_title="text title")

    def test_detail_view_contains_quote_title(self):
        response = self.client.get(reverse("essence:text_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.metadata.title)

    def test_detail_view_contains_quote_description(self):
        response = self.client.get(reverse("essence:text_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.metadata.description)

    def test_detail_view_contains_quote_text(self):
        response = self.client.get(reverse("essence:text_detail", args=(self.quote.pk,)))
        self.assertContains(response, self.quote.quote_text)