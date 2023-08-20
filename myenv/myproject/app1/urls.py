from django.urls import path,include
from.import views

urlpatterns = [
    path('index/',views.index,name='addform'),
    path('employe_list/',views.employe_list),
    path('emp_delete/<int:id>/',views.emp_delete,name='emp_delete'),
    path('emp_update/<int:id>/',views.emp_update,name='update'),
    path('emp_doupdate/<int:id>/',views.emp_doupdate,name='doupdate'),
    path('',views.register_view,name='register'),
    path('login/',views.login_view,name='login')
] 