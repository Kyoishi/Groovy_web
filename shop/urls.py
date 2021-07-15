from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('complete/', TemplateView.as_view(template_name='shop/complete.html'), name='complete'),
]
