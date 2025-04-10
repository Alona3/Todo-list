from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View  
from django.http import HttpResponseRedirect
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.all().order_by('is_done', '-created')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created = timezone.now()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse('task_list'))


class TagListView(ListView):
    model = Tag
    template_name = 'tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')
