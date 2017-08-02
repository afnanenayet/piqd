from django.db import models

# Data models for the suveys app

class Survey(models.Model):
    """The overarching model for a survey, which includes a set of questions 
    and some corresponding answers"""
    pub_date = models.DateTimeField("date published")

class Question(models.Model):
    """This is the data model for a question, multiple Questions are associated
    with a Survey in a many-to-one relationship"""
    survey = models.ForeignKey(Survey, on_delete = models.Cascade)
    question_text = models.CharField(max_length = 2000)

class Choice(models.Model):
    """An answer to a question (a multiple choice answer), multiple choices 
    are associated with a Question in a many-to-one relationship"""
    question = models.ForeignKey(Question, on_delete = models.Cascade)
    choice_text = models.CharField(max_length = 2000)
    votes = models.IntegerField(default = 0)

