from django.views import generic

from todo.models import Task, Tag


class HomeListView(generic.ListView):
    model = Task
    template_name = "todo/home_list.html"


class TagListView(generic.ListView):
    model = Tag
