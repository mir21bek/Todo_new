from django.urls import path
from . import views

urlpatterns = [
    path('todolist/', views.BlogCreateListView.as_view()),
    path('todolist/<int:pk>/', views.UpdateCreateDeleteListAPIView.as_view()),
    path('todolist/<int:pk>/complete/', views.StatusBlogList.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
]
