from django.urls import path
from .views import current_user, UserList,search_user

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('search/',search_user)
]