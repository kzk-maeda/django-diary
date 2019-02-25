"""
from django.db import models
from django.utils import timezone


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now())

    def __str__(self):
        return self.title
"""
import uuid
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
from django.utils import timezone


class Day(Model):
    id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()))
    title = UnicodeAttribute(range_key=True)
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=timezone.now())

    def __str__(self):
        return self.title
