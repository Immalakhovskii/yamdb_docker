from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Genre, Title, User, Review, Comment

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(User, UserAdmin)
admin.site.register(Review)
admin.site.register(Comment)
