from django.urls import path
from .views import index_view


app_name = 'new_ui'


urlpatterns = [
    path('', index_view)
]