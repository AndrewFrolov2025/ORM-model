from django.urls import path

from phones.views import catalog_view, phone_detail_view

urlpatterns = [
    path('', catalog_view, name='catalog'),
    path('catalog/', catalog_view, name='catalog'),
    path('catalog/<slug:slug>/', phone_detail_view, name='phone_detail'),
]