from django.urls import path
from todo.views import HomeListView, TagListView

app_name = "todo"

urlpatterns = [
    path("", HomeListView.as_view(), name="home_list"),
    path("tags/", TagListView.as_view(), name="tag_list"),
]

