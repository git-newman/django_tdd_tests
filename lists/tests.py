from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
from .views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    """тест на токсичность"""

    def test_home_page_returns_correct_html(self):
        """тест: домашняя страница возвращает правильный html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_post_request(self):
        """тест: пост может сохранить данные"""
        response = self.client.post('/', data={'item_text': 'a new list item'})
        self.assertIn('a new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
