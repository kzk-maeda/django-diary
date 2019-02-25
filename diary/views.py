from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import QueryDict
# from .forms import DayCreateForm
from .models import Day
import uuid


def index(request):
    day_list = Day.scan()
    context = {
        'day_list': day_list
    }
    return render(request, 'diary/day_list.html', context)


def add(request):
    if request.method == 'POST':
        response_dict = QueryDict(request.body)
        save_data = Day(
            str(uuid.uuid4()),
            title=response_dict['title'],
            text=response_dict['text'],
            created_at=timezone.now()
        )
        save_data.save()
        return redirect('diary:index')

    return render(request, 'diary/day_form.html')


def detail(request, pk):
    get_item_key = {"id": {"S": pk}}
    day = Day.get(str(pk))
    print(day)
    context = {
        'day': day
    }
    return render(request, 'diary/day_detail.html', context)
