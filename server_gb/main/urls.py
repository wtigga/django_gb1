from django.urls import path
from main.views import (main_view, about_view, contacts_view)

urlpatterns = [
    path('', main_view),
    path('about/', about_view),
    path('contacts/', contacts_view),
]
