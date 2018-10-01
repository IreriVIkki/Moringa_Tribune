from django.test import TestCase
from .models import Editor, tags, Article
import datetime as dt

# Create your tests here.


class EditorTestClass(TestCase):

    # setup function
    def setUp(self):
        self.victor = Editor(first_name='Victor',
                             last_name='Ireri', email='vikki@gmail.com')
        self.victor.save_editor()

        self.people = tags(name='people')
        self.people.save_tag()

        self.new_article = Article(
            title='Test Article', post='This is a random test Post', editor=self.victor)
        self.new_article.save_article()

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

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

    def test_get_news_today(self):
        todays_news = Article.todays_news()
        self.assertTrue(len(todays_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        # this line takes the test date passed and converts it to a datetime object
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
