from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # path('login/', views.user_login), # localhost:8000/account/login/ 경로, 경로를 호출하면 실행할 함수의 위치

    # 장고의 view 사용 tempates/registration/ 디렉터리와 연동됩니다.
    path('login/', auth_views.LoginView.as_view()), #
    path('logout/', auth_views.LogoutView.as_view()) # 주소로 접근해서 콘솔에 405가 뜨는 것 확인.
]