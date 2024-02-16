from django.urls import path
from task_manager.tasks import views


app_name = 'tasks'


urlpatterns = [
    path('', views.TasksView.as_view(), name='tasks'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    # path('<int:pk>/update/', views.UpdateStatusView.as_view(), name='update'),
    # path('<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete'),
    path('<int:pk>/', views.DetailTaskView.as_view(), name='task'),
]
