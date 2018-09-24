from django.test import TestCase
from .models import Editor, tags, Article

# Create your tests here.


class EditorTestClass(TestCase):

    # setup function
    def setUp(self):
        self.victor = Editor(first_name='Victor',
                             last_name='Ireri', email='vikki@gmail.com')
        self.people = tags(name='people')
        self.articleTest = Article()

    def test_instance(self):
        self.assertTrue(isinstance(self.victor, Editor))

    def test_save_editor(self):
        self.victor.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_editor(self):
        self.victor.save()
        self.victor.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)
