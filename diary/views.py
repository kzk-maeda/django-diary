from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import QueryDict
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
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        save_data.save()
        return redirect('diary:index')

    return render(request, 'diary/day_form.html')


def delete(request, pk):
    day = Day.get(str(pk))

    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    context = {
        'day': day
    }
    return render(request, 'diary/day_confirm_delete.html', context)


def update(request, pk):
    day = Day.get(str(pk))
    if request.method == 'POST':
        response_dict = QueryDict(request.body)
        save_data = Day(
            str(pk),
            title=response_dict['title'],
            text=response_dict['text'],
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        save_data.update_item()
        return redirect('diary:index')

    context = {
        'day': day
    }
    return render(request, 'diary/day_form.html', context)



def detail(request, pk):
    day = Day.get(str(pk))
    print(day)
    context = {
        'day': day
    }
    return render(request, 'diary/day_detail.html', context)
