from django.apps import AppConfig


class DiaryConfig(AppConfig):
    name = 'diary'

# Create DynamoDB Table

if not Day.exists():
    Day.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
