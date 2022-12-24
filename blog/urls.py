from django.urls import path
from . import views

urlpatterns = [
    # 페이지 번호 자동 지정
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
