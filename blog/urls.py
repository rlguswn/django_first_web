from django.urls import path
from . import views

urlpatterns = [
    # 페이지 번호 자동 지정
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view())
    # path('', views.index),
]
