import uuid
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)
from django.utils import timezone


class Day(Model):
    class Meta:
        table_name = "Day"
        host = "http://localhost:8000"
        region = 'ap-northeast-1'
        write_capacity_units = 1
        read_capacity_units = 1

    id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()))
    title = UnicodeAttribute()
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=timezone.now())
    updated_at = UTCDateTimeAttribute(default=timezone.now())

    def __str__(self):
        return self.title
