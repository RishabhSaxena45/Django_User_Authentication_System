from django.urls import path
from classbased import views


urlpatterns = [
    path('' , views.hello , name="hello"),
    path('home/' , views.home.as_view() , name="home"),
    path('form/' , views.FormView.as_view() , name="form"),
    path('create/' , views.studentcreate.as_view() , name="create"),
    path('list/' , views.studentlist.as_view() , name="list"),
    path('detail/<int:pk>' , views.studentdetail.as_view() , name="detail"),
    path('update/<int:pk>' , views.studentupdate.as_view() , name="update"),
    path('delete/<int:pk>' , views.studentdelete.as_view() , name="delete") 
]