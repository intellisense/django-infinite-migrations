# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=50)


class Child(models.Model):
    parent = models.ForeignKey('polls.Parent')

    class Meta:
        ordering = ('id', )
