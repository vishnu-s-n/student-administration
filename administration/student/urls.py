from django.urls import path
from student import views

urlpatterns = [
    path('add', views.student_form, name='student_form'),
    path('list',views.student_list,name="list")
]


