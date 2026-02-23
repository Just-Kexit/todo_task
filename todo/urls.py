from django.urls import path
from todo.views import TaskListView, TagListView, TaskCreateView

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/", TagListView.as_view(), name="tag_list"),
]

