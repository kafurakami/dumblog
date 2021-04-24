from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','body','author','header_image')

		widgets = {
			'title' : forms.TextInput(attrs = {'class': 'form-control'}),
			'body' : forms.Textarea(attrs = {'class': 'form-control'}),
			'author' : forms.TextInput(attrs = {'class': 'form-control', 'id':'user','value':'', 'type':'hidden'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('name','body')

		widgets = {
			'name' : forms.TextInput(attrs = {'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
			'body' : forms.Textarea(attrs = {'class': 'form-control'})
		}

	