from django.conf.urls import url
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from todolist.views import home, delete, edit, cross_off, uncross

class testurls(TestCase):

    def test_home(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.__name__, home.as_view().__name__)

# class testurls(SimpleTestCase):

#     def test_home(self):
#         url = reverse('home')
#         self.assertEquals(resolve(url).func, home)


#     def test_delete(self):
#         url = reverse('delete', args=['some-slug'])
#         self.assertEquals(resolve(url).func, delete)

#     def test_edit(self):
#         url = reverse('edit', args=['some-slug'])
#         self.assertEquals(resolve(url).func, edit)

#     def test_cross_off(self):
#         url = reverse('cross_off', args=['some-slug'])
#         self.assertEquals(resolve(url).func, cross_off)

#     def test_uncross(self):
#         url = reverse('uncross', args=['some-slug'])
#         self.assertEquals(resolve(url).func, uncross)
