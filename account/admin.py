from django.contrib import admin
from .models import User, Todo

# Register your models here.

@admin.register(User)
class UserAmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAmin(admin.ModelAdmin):
    pass

