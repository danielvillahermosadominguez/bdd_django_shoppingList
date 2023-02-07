from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from shoppinglistapi import views

item_url = [
    url(r'^([a-zA-Z][0-9a-zA-Z]{2,})/([1-9]+)/$', views.ShoppingListView.as_view(),  name='remove item'),
    url(r'^([a-zA-Z][0-9a-zA-Z]{2,})/$', views.ShoppingListView.as_view(),  name='add item'),
    url(r'^([a-zA-Z][0-9a-zA-Z]{2,})/([a-zA-Z][0-9a-zA-Z]{2,})/$', views.ShoppingListView.as_view(),  name='update item'),    
    url(r'^$', views.ShoppingListView.as_view(), name='list items')
]

urlpatterns = [
    path('', views.Info.as_view()),
    path('admin/', admin.site.urls),
    path('healthcheck/', views.HealthCheck.as_view()),
    path('items/', include(item_url)),
]
