from django.urls import path
from todo.views import HomeListView

app_name = "todo"

urlpatterns = [
    path("", HomeListView.as_view(), name="home_list"),
]

