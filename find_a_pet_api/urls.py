from django.urls import re_path as path
# from .User.user import CreateUserAPIView, LoginUserAPIView
from .views import user_login, user_signup
# user_logout
urlpatterns = [
  path('user_login/', user_login, name='user_login'),
  path('signup/', user_signup, name='signup'),  
]
