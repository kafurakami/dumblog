from django.urls import path
from .views import userregisterview, usereditview, passchangeview, profilepageview, editprofileview, createprofile
from . import views
#from django.contrib.auth import views as authviews No use now, see forms/py

urlpatterns = [
	path('register/', userregisterview.as_view(), name = 'register'),
	path('edit_account/', usereditview.as_view(), name = 'edit'),
	path('password/', passchangeview.as_view(), name = 'password'),
	path('passwordsuccess/', views.passwordsuccess, name = 'passwordsuccess'),
	path('<int:pk>/profile', profilepageview.as_view(), name = 'profile'),	
	path('<int:pk>/profile_update', editprofileview.as_view(), name = 'update'),
	path('create_profile', createprofile.as_view(), name = 'createprofile')

]