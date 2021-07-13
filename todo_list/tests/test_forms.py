from django.test import SimpleTestCase
from todo_list.forms import ListForm


class testforms(SimpleTestCase):

    def test_list(self):
        form = ListForm(data={
            'item': 'item05',
            'completed': False

        })
    
        self.assertTrue(form.is_valid())

    def test_list1(self):
        form = ListForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        