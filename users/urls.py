from django.urls import path
from .views import usersListView,usersDetailView

urlpatterns = [
    path('users/', usersListView),
    path('users<int:pk>',usersDetailView),

]
