from django.test import TestCase
from .models import Editor

# Create your tests here.


class EditorTestClass(TestCase):

    # setup function
    def setUp(self):
        self.victor = Editor(first_name='Victor',
                             last_name='Ireri', email='vikki@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.victor, Editor))
