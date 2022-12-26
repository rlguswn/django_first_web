from django.urls import path
from . import views

urlpatterns = [
    # 페이지 번호 자동 지정
    path('about_me/', views.about_me),
    path('', views.landing),
]
