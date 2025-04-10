from django.urls import path
from . import views

urlpatterns = [

    path('', views.TaskListView.as_view(), name='task_list'),

    path('tasks/add/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),

    path('tasks/<int:pk>/toggle/', views.ToggleTaskStatusView.as_view(), name='task_toggle'),

    path('tags/', views.TagListView.as_view(), name='tag_list'),

    path('tags/add/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
]
