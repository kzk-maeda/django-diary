from django.apps import AppConfig
from .models import Day


class DiaryConfig(AppConfig):
    name = 'diary'

# Create DynamoDB Table

if not Day.exists():
    Day.create_table(wait=True)
