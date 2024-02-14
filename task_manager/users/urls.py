from django.urls import path
from task_manager.users import views


app_name = 'users'


urlpatterns = [
    path('', views.UsersView.as_view(), name='users'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(), name='delete'),
]
