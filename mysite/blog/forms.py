from django import forms
from . models import Post, Comment, Shop, Visit

class PostForm(forms.ModelForm):
	class Meta:
		 model = Post
		 fields = ('title', 'content')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text')

class ShopForm(forms.ModelForm):
	class Meta:
		model = Shop
		fields = ('name', 'motto', 'advantages', 'contact_phone', 'email', 'base_style', 'banner_image')

class VisitForm(forms.ModelForm):
	class Meta:
		model = Visit
		fields = ('os', 'browser', 'device', 'ip', 'language', 'country', 'city', 'time_enter', 'time_escape', 'season', 'is_selebration', 'weather', 'day_of_the_week', 'mood', 'comment', 'result')