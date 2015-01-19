from django.contrib import admin
from jetapp.models import Category, Page
from jetapp.models import UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)