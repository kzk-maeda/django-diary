"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day
    template_name = "diary/day_detail.html"
"""
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
