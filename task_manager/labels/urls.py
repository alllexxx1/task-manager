from django.urls import path
from task_manager.labels import views


app_name = 'labels'


urlpatterns = [
    path('', views.LabelsView.as_view(), name='labels'),
    path('create/', views.CreateLabelView.as_view(), name='create'),
    # path('<int:pk>/update/', views.UpdateStatusView.as_view(), name='update'),
    # path('<int:pk>/delete/', views.DeleteStatusView.as_view(), name='delete'),
]
