import datetime

import tmdbsimple as tmdb
import requests

from django.db import models
from django.utils import timezone


'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
'''
class Movie(models.Model):
    Movie_id =models.IntegerField(blank=True)
    Movie_original_languag =models.CharField(max_length=4)
    Movie_original_title =models.CharField(max_length=100)
    Movie_overview = models.CharField(max_length=1000)
    Movie_popularity = models.IntegerField(blank=True)
    Movie_poster_path = models.CharField(max_length=100)
    Movie_release_date = models.DateField(blank=True)
    Movie_title = models.CharField(max_length=100)
