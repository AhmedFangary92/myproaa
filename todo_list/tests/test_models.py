from django.test import TestCase
from todo_list.models import List


class testmodels(TestCase):

    def setUp(self):
        self.list1 = List.objects.create(
            item = 'item 1',
            completed = False
        )

    def testpro(self):
        self.assertEquals(self.list1.item, 'item 1')