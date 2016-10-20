from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import Comment

admin.site.register(Post)
admin.site.register(Comment)