from django.contrib import admin
from registration.models import Profile

# Register your models here.

@admin.register(Profile)
class MegaProcessAdmin(admin.ModelAdmin):
    readonly_fields = ['user']