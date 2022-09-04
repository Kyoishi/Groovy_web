from django.urls import path
from django.views.generic import TemplateView
from . import views

# Add below
# reference: https://office54.net/python/django/image-file-upload
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    # Add register
    path('register/', views.register, name='register'),
    path('<int:book_id>/', views.detail, name='detail'),
    # path('update/<int:book_id>/', views.BookUpdateView.as_view(),name='update'),
    path('create-payment-intent/', views.payment, name='payment'),
    # path('complete/', TemplateView.as_view(template_name='shop/complete.html'), name='complete'),
]
# Add below
# reference: https://office54.net/python/django/image-file-upload
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
