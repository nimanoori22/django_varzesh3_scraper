from django.urls import path
from home import views
urlpatterns = [
    path('<int:id>/', views.postdetail, name='post_detail'),
]