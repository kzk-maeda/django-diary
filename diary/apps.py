from django.apps import AppConfig
from .models import Day
from django.utils import timezone
import uuid


class DiaryConfig(AppConfig):
    name = 'diary'

# Create DynamoDB Table
if not Day.exists():
    Day.create_table(wait=True)

# Save Initial Data
print(Day.scan())
save_data = Day(
    str(uuid.uuid4()),
    title="Sample Data 1",
    text="this is sample data 1.",
    created_at=timezone.now(),
    updated_at=timezone.now()
)
save_data.save()
