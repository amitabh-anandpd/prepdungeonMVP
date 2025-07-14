# prepdungeon/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Question, Waitlist

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'topic', 'subject', 'q_type', 'level')
    list_filter = ('q_type', 'subject', 'level')
    search_fields = ('question', 'topic', 'subject')

@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'created_at')

@admin.register(ContactUsEmail)
class ContactUsEmailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'created_at')
    list_filter = ('first_name', 'email', 'created_at')
    search_fields = ('namfirst_namee', 'email', 'created_at')
