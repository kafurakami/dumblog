from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserEditForm, ProfileCreationForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile

# Create your views here.

class createprofile(CreateView):
	model = Profile
	template_name = 'registration/createprofile.html' 
	form_class = ProfileCreationForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)
	#users id is passed to the form, and then the form is saved under that id

class editprofileview(UpdateView):
	model = Profile
	template_name = 'registration/updateprofile.html'
	fields = ['bio', 'profile_pic', 'facebook_url']
	success_url = reverse_lazy('homepage')

class profilepageview(DetailView):
	model = Profile
	template_name = 'registration/userprofile.html'

class userregisterview(CreateView):
	form_class = UserRegisterForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class usereditview(CreateView):
	form_class = UserEditForm
	template_name = 'registration/edit_settings.html'
	success_url = reverse_lazy('home')

class passchangeview(PasswordChangeView):
	form_class = PasswordChangeForm
	template_name = 'registration/password.html'
	success_url = reverse_lazy('passwordsuccess')

def passwordsuccess(request):
	return render(request, 'registration/success.html', {})