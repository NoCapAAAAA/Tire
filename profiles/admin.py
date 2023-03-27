from django.contrib import admin

from profiles.models import ClientProfile, Staff


@admin.register(ClientProfile, Staff)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'created_at', 'updated_at')
    search_fields = ('user', )