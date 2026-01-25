from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),
    path('employee/', views.employeeView.as_view()),
    path('employee/<int:pk>/', views.employeeDetailView.as_view()),
]
