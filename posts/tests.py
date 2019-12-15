from django.test import TestCase
from django.urls import reverse

from .models import Post
from .views import HomePageView


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.text}', 'just a test')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_view_url_by_name(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
