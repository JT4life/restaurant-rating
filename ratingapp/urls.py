from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('detail', views.detail, name="detail"),
    path('search', views.search, name="search"),
    path('post/<id>/', views.post, name='post-detail'),
    path('rating', views.rating, name='rating'),
    # path('detail', views.detail, name="detail"),
]
