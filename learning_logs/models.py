# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """ the topics of users' learning """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """ return strings to express models """
        return self.text


class Entry(models.Model):
    """specific knowledge about one topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """return strings of model"""
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text