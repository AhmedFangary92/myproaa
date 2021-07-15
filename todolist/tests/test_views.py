from django.test import TestCase
from django.urls import reverse
from todolist.models import List

class testviews(TestCase):

    def setUp(self):
        self.home_url = reverse('home')
        # self.uncross_url = reverse('uncross')
        
    def test_list_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # def test_uncross_GET(self):

    #     response = self.client.get(self.uncross_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'home.html')
