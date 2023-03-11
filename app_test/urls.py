from django.contrib import admin
from django.urls import path, include
from app_test.views import LoginView, AnswerView

app_name = 'app_test'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('answer/', AnswerView.as_view(), name='answer'),
]
