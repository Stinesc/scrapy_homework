from django.urls import path
from .views import IndexView

app_name = 'jeans_scraping'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
