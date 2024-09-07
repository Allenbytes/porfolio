# projects/admin.py
from django.contrib import admin
from .models import Inquiry, Project

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('created_at',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'date_posted')
    search_fields = ('title', 'description')
    list_filter = ('date_posted',)
    ordering = ('-date_posted',)
    readonly_fields = ('date_posted',)