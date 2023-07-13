# Imports
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLogInView, Registerpage
from django.contrib.auth.views import LogoutView
from base import views

# Creating URL Navigation Links
urlpatterns = [
    path('login/', CustomLogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Registerpage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('about/', views.about, name='about-us')

]
