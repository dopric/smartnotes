from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="home_index"),
    path('', views.HomeView.as_view()),
    path('about/', views.about, name="home_about")
]
