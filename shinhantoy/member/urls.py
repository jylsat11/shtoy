from django.urls import path
from . import views # 현재 폴더 안에서 views 를 가져온다.

urlpatterns = [
    #as_view라는 함수로 class based view를 전환
    path("", views.MemberRegisterView.as_view()),
    path("/password", views.MemberChangePasswordView.as_view()),
]