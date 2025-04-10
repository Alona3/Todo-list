from django.urls import path
from . import views


urlpatterns = [
    # Головна сторінка — список задач
    path('', views.task_list, name='task_list'),

    # Додавання, оновлення, видалення задач
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Зміна статусу задачі
    path('tasks/<int:pk>/toggle/', views.toggle_task_status, name='task_toggle'),

    # Сторінка тегів
    path('tags/', views.tag_list, name='tag_list'),

    # Додавання, оновлення, видалення тегів
    path('tags/add/', views.tag_create, name='tag_create'),
    path('tags/<int:pk>/update/', views.tag_update, name='tag_update'),
    path('tags/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
]
