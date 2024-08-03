from django.urls import path
from blog import views

urlpatterns = [
    path('', views.main, name='home'),
    path("about/", views.about, name="about"),
    path('cats/<slug:cat_slug>/', views.category, name='category')
]
