from django.urls import path
from blog import views

urlpatterns = [
    path('', views.main, name='home'),
    path('blog/', views.blog, name='blog'),
    path('project/', views.project, name='project'),
    path("about/", views.about, name="about"),
    path('blog/post/<int:post_id>', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name='category')
]
