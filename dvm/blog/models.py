from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null = True, blank = True, upload_to = "images/profiles/")
	facebook_url = models.CharField(max_length = 255, null = True, blank = True)
	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('homepage')


class Post(models.Model):
	title = models.CharField(max_length = 250)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	body = models.TextField()
	date = models.DateTimeField(auto_now = True)
	header_image = models.ImageField(null = True, blank = True, upload_to = "images")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('homepage')
		#returns back to the detail page with its own id like article/id after changes submitted successfully.

class Comments(models.Model):
	post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
	name = models.CharField(max_length = 255, null = True, blank = True)
	body = models.TextField()
	date = models.DateTimeField(auto_now = True)

	def __str__(self):
		return '%s - %s' % (self.post.title, self.name)

	def get_absolute_url(self):
		return reverse('homepage')

