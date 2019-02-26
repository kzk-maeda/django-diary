import os
import uuid
import logging
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)
from django.utils import timezone

logging.basicConfig()
log = logging.getLogger("pynamodb")
log.setLevel(logging.DEBUG)
log.propagate = True


class Day(Model):
    class Meta:
        table_name = "Day"
        # host = "http://localhost:8000"
        host = "http://dynamodb:8000"
        region = 'ap-northeast-1'
        write_capacity_units = 1
        read_capacity_units = 1
        aws_access_key_id = os.environ.get('ACCESS_KEY')
        aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY')

    id = UnicodeAttribute(hash_key=True, default=str(uuid.uuid4()))
    title = UnicodeAttribute()
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=timezone.now())
    updated_at = UTCDateTimeAttribute(default=timezone.now())

    def __str__(self):
        return self.title
