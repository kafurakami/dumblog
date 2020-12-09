from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from blog.models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 255)
	last_name = forms.CharField(max_length = 255)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserEditForm(UserChangeForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length = 255)
	last_name = forms.CharField(max_length = 255)
	username = forms.CharField(max_length = 255)
	last_name = forms.CharField(max_length = 255)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

class ProfileCreationForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('user','bio', 'profile_pic', 'facebook_url')

		widgets = {
			'user' : forms.TextInput(attrs = {'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
			'bio' : forms.Textarea(attrs = {'class': 'form-control'})
		}

