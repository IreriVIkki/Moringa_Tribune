from django.db import models
import datetime as dt

# Create your models here.


class Editor(models.Model):
    # charfields are like the equivalent of string field in flask
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()

    def delete_editor(self):
        # before you can delete an object you must fist fetch it from the database the delete it
        # If you dont you will be trying to delete an instance of the object that has not been saved which will never work aki ya mama
        editor = Editor.objects.get(pk=self.id)
        editor.delete()


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def delete_tag(self):
        tag = tags.objects.get(pk=self.id)
        tag.delete()

    def save_tag(self):
        self.save()


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    # i think this mf right here will add the current date and time of Article creation automatically by default
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/', blank=True)

    def __str__(self):
        return self.title

    def save_article(self):
        self.save()

    def delete_article(self):
        article = Article.objects.get(pk=self.id)
        article.delete()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, seart_term):
        news = cls.objects.filter(title__icontains=seart_term)
        return news


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
