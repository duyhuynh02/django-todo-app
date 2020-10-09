from django.test import TestCase 
from django.urls import reverse 
from django.contrib.auth import get_user_model 

from .models import Post 
import datetime


class TodoTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )


        self.post = Post.objects.create(
            title='A test title',
            memo='A test content',
            author=self.user,
            completed=False,
        )


    def test_string_represent(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)


    def test_post_component(self):
        self.assertEqual(f'{self.post.title}', 'A test title')
        self.assertEqual(f'{self.post.memo}', 'A test content')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.completed}', 'False')


    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A test content')
        self.assertTemplateUsed(response, 'home.html')


    def test_post_detail_view(self):
        response = self.client.get('/work/1')
        no_response = self.client.get('/work/100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A test title')
        self.assertTemplateUsed(response, 'work_detail.html')
