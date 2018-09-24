from django.db import models

# Create your models here.


class Editor(models.Model):
    # charfields are like the equivalent of string field in flask
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    # i think this mf right here will add the current date and time of Article creation automatically by default
    pub_date = models.DateTimeField(auto_now_add=True)
