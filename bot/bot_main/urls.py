from django.urls import path
from . import views
urlpatterns = [
    path('users/',views.users_view.as_view()),
    path('channel/<str:pk>/',views.channel_view.as_view()),
    path('give/',views.give_view.as_view()),
    path('admins/',views.admins_view.as_view()),
    path('asosiy/',views.asosiy_view.as_view()),
    path('channel_add/<str:telegram_id>/<str:username>/<str:title>/',views.channel_post),
    path('channel_edit/<str:telegram_id1>/', views.channel_edit),
    path('give_add/<str:give>/<str:channel_ids>/<str:admin>/',views.give_post),
    path('give_time/<str:give>/<str:time>/<str:admin>/', views.give_time),
    path('user_give/<str:telegram_id>/<str:username>/<str:name>/<int:give>/',views.user_add_to_give)
]