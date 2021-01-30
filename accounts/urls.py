from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register/',views.registeruser,name="register"),
    path('login/',views.loginuser,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('account/',views.account_view,name="account"),
    path('vote/',views.voter,name="voter"),
    path('verifyvoter/',views.verifyvoter,name="verifyvoter"),
    path('deletebjp/',views.votedbjg,name="votedbjp"),
    path('deletemns/',views.votedmns,name="votedmns"),
    path('deletecong/',views.votedcongress,name="votedcongress"),
    
     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
