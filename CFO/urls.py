from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('',views.home,name='login-page'),
    path('createtask',views.CTask,name='create_task'),
    path('login1',views.login1,name='login1'),
    path('register',views.Register,name='User-Register'),
    path('Reg', views.Reg,name='reg_user'),
    path('log', views.log,name='Login_process'),
    path('logout', views.logout,name='Logout_process'),
    path('viewuser', views.Viewuser,name='view_user'),
    path('Dashuser', views.Dashuser,name='Dash_user'),
    path('work_on/<str:id>', views.Working,name='Working'),
    path('complete/<str:id>', views.Completed,name='completed'),
    path('COEApproveUser', views.COEApproveUser,name='COEApproval'),
    path('COEAssignTask', views.COEAssignTask,name='COEassignTask'),
    path('COEInsights', views.COEInsights,name='COEinsights'),
    path('COEViewUsers', views.COEViewUsers,name='COEviewusers'),
    path('COEAddUser', views.COEAddUsers,name='COEaddusers'),
    path('CLAU', views.LUserAdd,name='LeadsAddingUser'),
    path('Cuserdash/<str:id>', views.UserTask,name='Userwise Task'),
    path('active/<str:id>', views.ApproveUser,name='ApproveUser'),
    path('deactive/<str:id>', views.BlockedUser,name='BlockedUser'),
    path('assign/<str:id>', views.COEAssignTaskUser,name='COE_Assign_TaskUser'),
]
