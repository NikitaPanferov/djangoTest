from django.urls import path

from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_url>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_url>', MainCategory.as_view(), name='category'),
    path('logout', logout_user, name='logout'),
    path('add_post', AddPost.as_view(), name='add_post'),
]